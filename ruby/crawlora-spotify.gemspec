require_relative "lib/crawlora/spotify/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-spotify"
  spec.version = Crawlora::Spotify::VERSION
  spec.summary = "Spotify API client for Crawlora (38 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Spotify API. Covers search, tracks, albums, artists, playlists, profiles, audiobooks, charts, and podcast shows and episodes across 38 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-spotify", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-spotify/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
