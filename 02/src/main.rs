use std::fs;

fn main() {
    let content = fs::read_to_string("input").expect("Nope");

    let part1 = part1(&content);
    println!("{}", part1);

    let part2 = part2(&content);
    println!("{}", part2)
}

fn part1(content: &String) -> i32 {
    let mut depth: i32 = 0;
    let mut horizontal: i32 = 0;
    for line in content.lines() {
        if line.contains("forward") {
            horizontal += &line[8..9].parse::<i32>().unwrap();
        } else if line.contains("down") {
            depth +=  &line[5..6].parse::<i32>().unwrap();
        } else if line.contains("up") {
            depth -= &line[3..4].parse::<i32>().unwrap();
        }
    }
    return depth * horizontal
}

fn part2(content: &String) -> i32 {
    let mut depth: i32 = 0;
    let mut horizontal: i32 = 0;
    let mut aim: i32 = 0;
    for line in content.lines() {
        if line.contains("forward") {
            horizontal += &line[8..9].parse::<i32>().unwrap();
            depth += &aim * &line[8..9].parse::<i32>().unwrap();
        } else if line.contains("down") {
            aim += &line[5..6].parse::<i32>().unwrap();
        } else if line.contains("up") {
            aim -= &line[3..4].parse::<i32>().unwrap();
        }
    }
    return depth * horizontal
}