use rand::Rng; // Simulate random success/failure of API calls
use std::thread;
use std::time::Duration;

// Simulated API call to gpt-3.5-turbo
fn call_gpt_3_5_turbo() -> Result<&'static str, &'static str> {
    if rand::thread_rng().gen_range(0..10) > 2 { // 70% chance of failure to simulate an error
        Err("gpt-3.5-turbo failed")
    } else {
        Ok("Success from gpt-3.5-turbo")
    }
}

// Simulated API call to gpt-4-turbo-preview
fn call_gpt_4_turbo_preview() -> Result<&'static str, &'static str> {
    if rand::thread_rng().gen_range(0..10) > 5 { // 50% chance of failure
        Err("gpt-4-turbo-preview failed")
    } else {
        Ok("Success from gpt-4-turbo-preview")
    }
}

// Function that attempts to call gpt-3.5-turbo up to 3 times before falling back to gpt-4-turbo-preview
fn attempt_api_calls() -> Result<&'static str, &'static str> {
    let mut attempts = 0;
    loop {
        match call_gpt_3_5_turbo() {
            Ok(success) => return Ok(success),
            Err(_) if attempts < 2 => {
                attempts += 1;
                println!("Retrying gpt-3.5-turbo... Attempt {}", attempts);
                thread::sleep(Duration::from_secs(1)); // Simulate delay before retrying
            },
            Err(_) => break, // Breaks the loop to fallback to gpt-4-turbo-preview
        }
    }

    // Fallback to gpt-4-turbo-preview after failing with gpt-3.5-turbo
    match call_gpt_4_turbo_preview() {
        Ok(success) => Ok(success),
        Err(e) => Err(e),
    }
}

fn main() {
    match attempt_api_calls() {
        Ok(result) => println!("API call successful: {}", result),
        Err(e) => println!("All API calls failed: {}", e),
    }
}
