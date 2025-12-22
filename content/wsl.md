Title: WSL (Windows Subsystem for Linux)
Date: 2025-09-02
Category: Linux
Slug: wsl
Summary: Working with WSL and Windows file system integration

### Common Paths

| Windows Path | WSL Path |
|--------------|----------|
| `C:\Users\username` | `/mnt/c/Users/username` |
| `D:\Projects` | `/mnt/d/Projects` |
| WSL home | `\\wsl$\Ubuntu\home\username` (from Windows) |

### Accessing Windows Files from WSL

Windows drives are mounted under `/mnt/` in WSL. Your C: drive is at `/mnt/c/`.

```bash
# Navigate to Windows user directory
cd /mnt/c/Users/your-username/Documents

# List files
ls -la
```

### Opening Windows File Explorer from WSL

```bash
# Open Explorer at current WSL directory
explorer.exe .
```

### Accessing WSL Files from Windows

In Windows File Explorer, type `\\wsl$\` in the address bar. This shows all installed WSL distributions and their file systems.

### Create Shortcuts with Symbolic Links

```bash
# Create a symlink to quickly access Windows folders
ln -s /mnt/c/Users/your-username/workproducts ~/winwork

# Now just use
cd ~/winwork
```

### Performance Tips

- **Keep project files in WSL filesystem** (`/home/...`) for best performance
- **Avoid heavy I/O across filesystems** - accessing `/mnt/c/` is slower than native WSL paths
- **Use WSL 2** for better file system performance with Linux-native filesystems
