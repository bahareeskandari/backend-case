#!/bin/sh

# Inject environment variables into the frontend at runtime
echo "Setting up environment variables..."
echo "window.env = { VITE_API_URL: \"$VITE_API_URL\" };" > /usr/share/nginx/html/env-config.js

# Debugging: Print the generated config file
cat /usr/share/nginx/html/env-config.js

# Start nginx
nginx -g "daemon off;"
