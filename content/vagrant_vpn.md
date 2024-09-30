Title: Vagrant VM with VPN
Date: 2017-12-03
Category: Linux
Slug: Vagrant VM with VPN
Summary: Vagrant VM with VPN setup

## Step-by-Step Instructions to Set Up a VM to Bypass Zscaler Restrictions

#### 1. **Create a DigitalOcean Droplet with Outline VPN Manager**

1. Set up a new DigitalOcean droplet.
2. Install Outline VPN Manager to manage the Shadowsocks server. Follow the official Outline installation guide for setup.
3. Note the public IP address of your DigitalOcean server.

#### 2. **Install and Configure Shadowsocks on the DigitalOcean Server**

1. Install Shadowsocks on the server:
   ```bash
   sudo apt update
   sudo apt install shadowsocks-libev
   ```

2. Edit the default Shadowsocks configuration (`/etc/shadowsocks-libev/config.json`) to use port `443` and your custom password:
   ```json
   {
     "server": "0.0.0.0",
     "server_port": 443,
     "password": "your-secure-password",
     "timeout": 60,
     "method": "chacha20-ietf-poly1305"
   }
   ```

3. Restart the Shadowsocks server:
   ```bash
   sudo systemctl restart shadowsocks-libev
   ```

4. Ensure that port `443` is open on the DigitalOcean server by allowing it through the firewall:
   ```bash
   sudo ufw allow 443/tcp
   sudo ufw allow 443/udp
   ```

#### 3. **Configure Shadowsocks Client on the Vagrant Guest VM**

1. Install Shadowsocks on the Vagrant guest VM:
   ```bash
   sudo apt update
   sudo apt install shadowsocks-libev
   ```

2. Create the Shadowsocks client configuration (`/etc/shadowsocks-libev/config.json`) to connect to the DigitalOcean server:
   ```json
   {
     "server": "your-digital-ocean-server-ip",
     "server_port": 443,
     "local_port": 1080,
     "password": "your-secure-password",
     "timeout": 60,
     "method": "chacha20-ietf-poly1305"
   }
   ```

3. Start the Shadowsocks client on the Vagrant VM:
   ```bash
   ss-local -c /etc/shadowsocks-libev/config.json -v
   ```

4. Ensure the Vagrant VM is using **Bridged Adapter** to allow direct internet access and connection to the DigitalOcean server.

#### 4. **Configure the Vagrant VM or Browser to Use the SOCKS Proxy**

1. Set the system or application (e.g., web browser) to use `localhost:1080` as the SOCKS5 proxy.
2. For Firefox:
   - Go to **Preferences** → **Network Settings**.
   - Set **SOCKS Host** to `localhost` and port to `1080`.
   - Ensure **SOCKS v5** is selected.

#### 5. **Test the Connection**

1. Verify that traffic is routed through the Shadowsocks proxy by browsing or using:
   ```bash
   curl --socks5 localhost:1080 http://example.com
   ```

2. Ensure that you can bypass Zscaler restrictions and access unrestricted internet.

#### Summary:
- DigitalOcean droplet runs **Outline VPN Manager** and Shadowsocks on **port 443**.
- **Vagrant guest VM** connects via Shadowsocks client using `ss-local` with port `443`.
- **Bridged Adapter** mode is essential for proper networking in the VM.
- SOCKS5 proxy runs locally on `localhost:1080` to bypass restrictions.

This setup allows you to route traffic through your DigitalOcean server, effectively bypassing Zscaler restrictions.


## Updated Step-by-Step Solution for Bypassing Zscaler Using the Vagrant Guest VM

Since you want to use **Firefox on the Vagrant guest VM** to bypass restrictions without relying on any executable files on the Windows host, we’ll configure the VM and Firefox to directly route traffic through the Shadowsocks proxy.

#### Step 1: Ensure Shadowsocks is Set Up on the DigitalOcean Server
Make sure your **DigitalOcean server** is configured and running properly.

1. **DigitalOcean Server Shadowsocks Configuration (`/etc/shadowsocks-libev/config.json`):**

   ```json
   {
     "server": "0.0.0.0",
     "server_port": 443,            // Running on port 443 to avoid network restrictions
     "password": "your-secure-password",
     "timeout": 60,
     "method": "chacha20-ietf-poly1305"
   }
   ```

2. **Restart the Shadowsocks server** on the DigitalOcean droplet:
   ```bash
   sudo systemctl restart shadowsocks-libev
   ```

#### Step 2: Set Up Shadowsocks on the Vagrant Guest VM
Ensure the Shadowsocks client is installed and running on the **guest VM**.

1. **Install Shadowsocks on the Guest VM**:
   ```bash
   sudo apt update
   sudo apt install shadowsocks-libev
   ```

2. **Create or update the client configuration file (`/etc/shadowsocks-libev/config.json`)**:
   ```json
   {
     "server": "your-digital-ocean-server-ip",   // The public IP of your DigitalOcean server
     "server_port": 443,                         // Port 443 to avoid network restrictions
     "local_port": 1080,                         // The local SOCKS5 proxy port
     "password": "your-secure-password",         // Same as on the server
     "timeout": 60,
     "method": "chacha20-ietf-poly1305"          // Same encryption method as the server
   }
   ```

3. **Start the Shadowsocks client** on the guest VM:
   ```bash
   ss-local -c /etc/shadowsocks-libev/config.json -v
   ```

   This command starts the Shadowsocks SOCKS5 proxy on `localhost:1080` on your VM.

#### Step 3: Configure Firefox on the Guest VM to Use the SOCKS Proxy

1. **Open Firefox** on the Vagrant guest VM.
2. Go to **Preferences** → Scroll down to **Network Settings** → Click **Settings**.
3. **Set up the SOCKS Proxy**:
   - Choose **Manual proxy configuration**.
   - Under **SOCKS Host**, enter `localhost` and set the port to `1080`.
   - Select **SOCKS v5** as the protocol.
   - Check the box for **Proxy DNS when using SOCKS v5**.

   ![Firefox Proxy Settings](https://support.mozilla.org/en-US/kb/connection-settings-firefox/windows-firefox-proxy-settings-windows.png) (Example of Firefox manual proxy settings).

4. **Save** the settings.

Now, all traffic from Firefox will be routed through the SOCKS5 proxy running on your Vagrant guest VM, which connects to your DigitalOcean Shadowsocks server. This should bypass any Zscaler restrictions.

#### Step 4: Test the Setup

1. Open Firefox on the guest VM and visit a website that is typically restricted by Zscaler.
2. Ensure the site loads, confirming that the traffic is routed through your DigitalOcean server and bypassing Zscaler.

### Additional Steps (If Needed)

#### Disable Ethernet on Host to Prevent Automatic Connection
Since your **office screens automatically connect to Ethernet**, you can disable the Ethernet interface temporarily on the **Windows host** to force all traffic through your guest VM.

1. On your **Windows host**, disable Ethernet:
   - Press `Win + R`, type `ncpa.cpl`, and press **Enter**.
   - Right-click on the **Ethernet** adapter and choose **Disable**.

   This will prevent the automatic Ethernet connection when using office screens, forcing your internet traffic through the Vagrant guest VM.

#### Summary of Steps:

1. **DigitalOcean Server**:
   - Ensure Shadowsocks is running on port `443`.
   
2. **Vagrant Guest VM**:
   - Start Shadowsocks with `ss-local` on `localhost:1080`.
   - Configure Firefox to use `localhost:1080` as a SOCKS5 proxy.

3. **Test**: Open restricted sites in Firefox on the guest VM to confirm Zscaler is bypassed.

This setup ensures that all traffic from Firefox is routed through the Vagrant guest VM and Shadowsocks, bypassing the Zscaler restrictions when connected to the office Ethernet. Let me know if you need further adjustments!
