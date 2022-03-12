require "discordcr"

module Persona
  VERSION = "0.1.0"
  
  client = Discord::Client.new(token: "") # Insert your Discord account token here
  cache = Discord::Cache.new(client)
  client.cache = cache

  # The bot replies to '~/ping' with 'Pong' and '~/pong' with 'Ping' 
  client.on_message_create do |payload|
    if payload.content.starts_with? "~/ping"
      client.create_message(payload.channel_id, "Pong! :gem:")
    end
    if payload.content.starts_with? "~/pong"
      client.create_message(payload.channel_id, "Ping! :sparkles:")
    end
  end

  client.run
end
