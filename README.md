# Spotify clients for Crawlora

Official Crawlora client packages for the hosted Spotify API. These clients call Crawlora's hosted API; they do not scrape Spotify locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Spotify or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/spotify`](javascript/README.md)
- Python: [`crawlora-spotify`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-spotify`](go.mod)
- Ruby: [`crawlora-spotify`](ruby/README.md)
- Java: [`net.crawlora:crawlora-spotify:0.1.0`](java/README.md)
- PHP: [`crawlora/spotify`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage

The six clients provide access to 38 public API operations. See the [API reference](docs/usage.md) for supported operations, parameters, and response details.

## License

MIT. See [LICENSE](LICENSE).
