use std::io;
use reqwest::{Client, Url};

const FLAG: &str = "flag{Y0uS3rv3d!th4t5Bl00dyNiceInnit?}";
const NOT_FLAG: &str = "That's not tea!! That's coffee!! Ugh...";
fn get_out_message(response_code: i32) -> &'static str {
    return if response_code == 418 { FLAG } else { NOT_FLAG };
}

#[tokio::main]
async fn main() {
    println!("I need tea, would you be a gentleman and give me the link:");
    loop {
        let mut url_entered = String::new();
        io::stdin().read_line(&mut url_entered).expect("Invalid string");
        let client = Client::builder().danger_accept_invalid_certs(true).build().unwrap();
        let trimmed_url = url_entered.trim();

        let url = match Url::parse(trimmed_url) {
            Ok(parsed_url) => parsed_url,
            Err(_) => {
                match Url::parse(&format!("https://{}", trimmed_url)) {
                    Ok(default_scheme_url) => default_scheme_url,
                    Err(_) => {
                        println!("I believe this is not the right format for thy proposition");
                        continue;
                    }
                }
            }
        };
        let resp = match client.get(url).send().await {
            Ok(response) => response,
            Err(_) => {
                println!("That is believe to be the right format for thy proposition, but I am afraid I am not able to perform thus task");
                continue;
            }
        };
        let status_code = resp.status().as_u16();
        println!("{}", get_out_message(status_code as i32));
        if status_code == 418 {
            std::process::exit(0);
        }
    }
}
