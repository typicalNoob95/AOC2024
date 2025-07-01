use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

enum ReportSafety {
    Safe,
    FailurePoint(usize)
}
fn report_is_safe(report: &Vec<&str>) -> ReportSafety{
    let mut previous_level: i32 = i32::max_value();
    let mut ascending: bool = true;
    let max_increment: i32 = 3;
    let min_increment: i32 = 1;

    for i in 0..report.len() {
        let level = report[i].parse::<i32>().unwrap();
        if i == 0 {
            previous_level = level;
            if level > report[i+1].parse::<i32>().unwrap() {
                ascending = false;
            }
        } else {
            let increment = level - previous_level;
            if (increment.abs() < min_increment) || (increment.abs() > max_increment){
                return ReportSafety::FailurePoint(i);
            }
            if increment < 0 && ascending{
                return ReportSafety::FailurePoint(i);
            }
            if increment > 0 && !ascending{
                return ReportSafety::FailurePoint(i);
            }
            previous_level = level;
        }
    }
    return ReportSafety::Safe;
}


fn main() {
    let problem_file: File = File::open(r"D:\ProjetsProgrammation\2024\AOC2024\problem_files\day_02\input.txt").unwrap();
    let file_reader = BufReader::new(problem_file);
    let mut number_of_safe_reports: i32 = 0;
    let mut number_of_safe_reports_with_dampener: i32 = 0;

    for line in file_reader.lines() {
        let report_line = match line {
            Ok(line) => line,
            Err(e) => panic!("{}", e)
        };

        let report = report_line.split(" ").collect::<Vec<&str>>();

        match report_is_safe(&report) {
            ReportSafety::Safe => {
                number_of_safe_reports += 1;
            },
            ReportSafety::FailurePoint(index) => {
                let mut modified_report: Vec<&str> = Vec::new();
                for i in 0..report.len() {
                    if i != index {
                        modified_report.push(report[i]);
                    }
                }
                match report_is_safe(&modified_report) {
                    ReportSafety::Safe => {
                        number_of_safe_reports_with_dampener += 1;
                    }
                    ReportSafety::FailurePoint(_) => {

                    }
                }
            }
        }


    }
    println!("There are {} safe reports", number_of_safe_reports);
    println!("There are {} safe reports with the problem dampener", (number_of_safe_reports + number_of_safe_reports_with_dampener));
}
