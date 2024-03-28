// Web Crawler in Go
// Http Client & Web Crawler
package main

use rand::{thread_rng, Rng}; // Add this to Cargo.toml under [dependencies]

/// Executes a risky operation by randomly selecting an AI model.
/// Returns `Ok` with a model code on success or `Err` with a message on failure.
fn select_model() -> Result<&'static str, &'static str> {
    let models = ["gpt-3.5-turbo-0125", "gpt-4-turbo-preview", "gpt-3.5-turbo"];
    let mut rng = thread_rng();

    if rng.gen_bool(0.5) { // 50% chance of success
        let model = models[rng.gen_range(0..models.len())];
        Ok(model)
    } else {
        Err("Operation failed")
    }
}

/// Main function demonstrating the use of `risky_operation`.
fn main() {
    match risky_operation() {
        Ok(model) => println!("Selected model: {}", model),
        Err(e) => println!("Error: {}", e),
    }
}

