use async_openai::{Client, config::OpenAIConfig};

let client = client::new();

let api_key = "";
let config = OpenAIConfig::default();
let client = Client::with_config(config);

let client = Client::with_config(config);

// Use custom reqwest client
let http_client = reqwest::ClientBuilder::new().user_agent("async-openai").build().unwrap();
let client = Client::new().with_http_client(http_client);