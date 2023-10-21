use std::env;
use std::fs::File;
use std::io::{self, Read};
use std::time::Instant;
use sysinfo::{CpuExt, System, SystemExt};

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
    let mut sys = System::new();
    let mut total_usage = 0.0;


    let start_time = Instant::now();

    let word_count = count_words(filename)?;

    sys.refresh_all();
    for cpu in sys.cpus() {
         total_usage += cpu.cpu_usage();
    }
    // Sleeping to let time for the system to run for long
    // enough to have useful information.
    std::thread::sleep(System::MINIMUM_CPU_UPDATE_INTERVAL);


    let end_time = Instant::now();
    let execution_time = end_time - start_time;
    let average_usage = total_usage / sys.cpus().len() as f32;

    println!("Word count: {}", word_count);
    println!("Time taken: {}.{:03} seconds", execution_time.as_secs(), execution_time.subsec_millis());
    println!("Average CPU core usage: {:.2}%", average_usage);
    println!("Memory usage: {} kilobytes", sys.total_memory() / 1000000);

    Ok(())
}
