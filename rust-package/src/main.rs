use std::env;
use std::fs::File;
use std::io::{self, Read};
use std::time::Instant;

fn count_words(filename: &str) -> io::Result<usize> {
    let mut file = File::open(filename)?;
    let mut text = String::new();
    file.read_to_string(&mut text)?;

    let words: Vec<&str> = text.split_whitespace().collect();
    Ok(words.len())
}

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: {} <filename>", args[0]);
        std::process::exit(1);
    }

    let filename = &args[1];

    let start_time = Instant::now();
    let word_count = count_words(filename)?;
    let elapsed_time = start_time.elapsed();

    println!("Word count: {}", word_count);
    println!("Time taken: {}.{:03} seconds", elapsed_time.as_secs(), elapsed_time.subsec_millis());

    Ok(())
}

