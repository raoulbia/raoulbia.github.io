Title: Fullstack Dev Notes
Date: 2024-07-18
Category: AI
Slug: fullstack
Summary: Fullstack Dev Notes

<br>

## Managing API_HOST Environment Variable in Next.js Projects

When developing a Next.js application, it's crucial to manage environment variables effectively, especially for differentiating between local testing and production deployments. This article will guide you through setting up and handling the `API_HOST` environment variable using the `next.config.mjs` file and CI/CD pipeline configurations with YAML files.

### 1. Configuring `API_HOST` in `next.config.mjs`

The `next.config.mjs` file is the central configuration file for a Next.js application. You can use it to define the `API_HOST` environment variable, ensuring it points to the correct URL based on the environment.

#### Example Configuration:

```javascript
const isProd = process.env.NODE_ENV === 'production';

module.exports = {
  env: {
    API_HOST: isProd ? 'https://api.productionurl.com' : 'http://localhost:3000',
  },
};
```

In this setup:
- If `NODE_ENV` is set to 'production', `API_HOST` will be assigned the production URL.
- For any other environment, it defaults to the localhost URL, suitable for local testing.

### 2. Setting `API_HOST` in `frontend_build_deploy.yml`

This YAML file is typically used for CI/CD pipelines to build and deploy the frontend application. You can define steps to set environment variables before running the build and deploy steps.

#### Example `frontend_build_deploy.yml`:

```yaml
name: Frontend Build and Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm install

    - name: Set API_HOST
      run: echo "API_HOST=https://api.productionurl.com" >> $GITHUB_ENV

    - name: Build
      run: npm run build

    - name: Deploy
      run: npm run deploy
```

In this example:
- The `Set API_HOST` step sets the `API_HOST` environment variable for the build process.
- The $GITHUB_ENV file is created automatically by GitHub Actions. You do not need to manually create this file or define it in your GitHub repository's secrets.

### 3. Setting `API_HOST` in `backend_build_deploy.yml`

Similarly, you can manage environment variables for the backend application using a CI/CD pipeline configuration.

#### Example `backend_build_deploy.yml`:

```yaml
name: Backend Build and Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm install

    - name: Set API_HOST
      run: echo "API_HOST=https://api.productionurl.com" >> $GITHUB_ENV

    - name: Build
      run: npm run build

    - name: Deploy
      run: npm run deploy
```

In this setup:
- The `Set API_HOST` step sets the `API_HOST` environment variable for the backend build process.

### Conclusion

By configuring the `API_HOST` environment variable in `next.config.mjs` and utilizing CI/CD pipelines with YAML files, you can ensure your Next.js application seamlessly transitions between local testing and production environments. This approach helps maintain consistency and reliability across different deployment stages.

<br>

## Deploying Next.js Applications to Azure as a Web App and Web Service

When deploying a Next.js application to Azure, it's essential to ensure that environment variables like `API_HOST` are correctly configured for both backend (web app) and frontend (web service) deployments. Here’s how to handle this in Azure:

## Setting Up Environment Variables in Azure Web App (Backend)

1. **Navigate to the Azure portal** and select your Web App.
2. **Go to the Configuration** under the **Settings** section.
3. **Add a new application setting**:
   - **Name**: `API_HOST`
   - **Value**: `https://api.productionurl.com` (or your actual production API URL)
4. **Save the changes** and restart the Web App.

## Setting Up Environment Variables in Azure Web Service (Frontend)

1. **Navigate to the Azure portal** and select your Web Service.
2. **Go to the Configuration** under the **Settings** section.
3. **Add a new application setting**:
   - **Name**: `API_HOST`
   - **Value**: `https://api.productionurl.com` (or your actual production API URL)
4. **Save the changes** and restart the Web Service.

