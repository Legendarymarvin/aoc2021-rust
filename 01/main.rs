use std::fs;

fn main() {
    let content = fs::read_to_string("input").expect("Nope");
    let lines: Vec<i32> = content.lines().map(|line| line.parse().unwrap()).collect();

    let counter1 = part1(&lines);
    println!("{}", counter1);

    let counter2 = part2(&lines);
    println!("{}", counter2)
}

fn part2(lines: &Vec<i32>) -> i32 {
    let mut counter2 = 0;
    for (i, _) in lines.iter().enumerate() {
        if i >= lines.len() - 3 {
            break;
        }
        if (lines[i + 1] + lines[i + 2] + lines[i + 3]) > (lines[i] + lines[i + 1] + lines[i + 2]) {
            counter2 += 1;
        }
    }
    counter2
}

fn part1(lines: &Vec<i32>) -> i32 {
    let mut counter1 = 0;
    for (i, line) in lines.iter().enumerate() {
        if i >= lines.len() - 1 {
            break;
        }
        if lines[i + 1] > *line {
            counter1 += 1;
        }
    }
    counter1
}