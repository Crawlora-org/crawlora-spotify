use crawlora_spotify::{Client, ModelSpotifySearchCatalogResponseDoc, SpotifySearchParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .spotify
        .search(SpotifySearchParams {
            q: Some("daft punk".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelSpotifySearchCatalogResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
