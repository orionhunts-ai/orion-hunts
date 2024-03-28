use async_openai::{Client, types::{CreateCompletionRequestArgs}};

let client = Client.new();

// Use custom reqwest client
let http_client = reqwest::ClientBuilder::new().user_agent("async-openai").build().unwrap();
let client = Client::new().with_http_client(http_client);

use async_openai::{Client, types::{CreateCompletionRequestArgs}};

 // Create client
 let client = Client::new();

 // Create request using builder pattern
 // Every request struct has companion builder struct with same name + Args suffix
 let request = CreateCompletionRequestArgs::default()
     .model("gpt-3.5-turbo")
     .prompt("Tell me the recipe of alfredo pasta")
     .max_tokens(40_u16)
     .build()
     .unwrap();

 // Call API
 let response = client
     .completions()      // Get the API "group" (completions, images, etc.) from the client
     .create(request)    // Make the API call in that "group"
     .await
     .unwrap();

# /modules/data_processor.py
import aiohttp
from config.settings import API_TIMEOUT

async def fetch_data(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=API_TIMEOUT) as response:
            return await response.text()

 println!("{}", response.choices.first().unwrap().text);
