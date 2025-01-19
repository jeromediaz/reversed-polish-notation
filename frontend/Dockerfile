# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN yarn install

# Copy the rest of the application code to the container
COPY . .

# Build the React application for production
RUN yarn run build

# Use an official Nginx image to serve the built app
FROM nginx:stable-alpine
COPY --from=0 /app/build /usr/share/nginx/html

# Expose the port Nginx will serve on
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]