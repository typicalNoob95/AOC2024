use std::cmp::{max, min};
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::ops::Index;

fn parse_left_and_right_list(left_list: &mut Vec<i32>, right_list: &mut Vec<i32>, line: String) 
{
    let chars: Vec<&str> = line.split("   ").collect();
    left_list.push(chars.index(0).parse::<i32>().unwrap());
    right_list.push(chars.index(1).parse::<i32>().unwrap());
}


fn main()
{
    let mut left_list: Vec<i32> = Vec::new();
    let mut right_list: Vec<i32> = Vec::new();
    
    //let sample_file: &str = "/home/fl/programming/aoc2024/problem_files/day_01/sample.txt";
    let input_file: &str = "/home/fl/programming/aoc2024/problem_files/day_01/input.txt";
    
    let problem_file = File::open(input_file).expect("Failed to open input file");
    let problem_lines = BufReader::new(problem_file).lines();
    for line in problem_lines
    {
        match line
        {
            Ok(line) => parse_left_and_right_list(&mut left_list, &mut right_list, line),
            Err(e) => panic!("{}", e),
        };
    }
    
    left_list.sort();
    right_list.sort();
    
    let len_of_lists :usize = left_list.len();
    let mut total_distance: i32 = 0;
    let mut similarity : i32 = 0;
    for i in 0..len_of_lists
    {
        let maximum = max(left_list[i], right_list[i]);
        let minimum = min(left_list[i], right_list[i]);
        let distance = maximum - minimum;
        total_distance += distance;
        
        let sim_search: i32 = left_list[i];
        let mut number_of_similarities: i32 = 0;
        for element in right_list.iter()
        {
            if element == &sim_search
            {
                number_of_similarities += 1;
            }
        }
        similarity += number_of_similarities * sim_search;
    }
    
    println!("Total distance: {}", total_distance);
    println!("similarity: {}", similarity);
}
