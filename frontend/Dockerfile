# syntax=docker/dockerfile:1.4
FROM node:16.14.0-buster-slim

# Create app directory
WORKDIR /frontend

# Install package.json from ark directory and run npm install
COPY ./package.json ./
RUN yarn install

# Copy app code
COPY . .

# Build app
RUN npm run build

# Expose port 8888 for React app
EXPOSE 8888

# Run React app
CMD ["npm", "start"]