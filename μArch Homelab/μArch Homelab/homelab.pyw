from modulecheck import *


def open_apps():
    username = os.getenv("USERNAME")
    apps = [
        {"name": "Zoom", "path": rf"C:\Users\{username}\AppData\Roaming\Zoom\bin\Zoom.exe"},
        {"name": "Google Chrome", "path": r"C:\Program Files\Google\Chrome\Application\chrome.exe"},
    ]
    for app in apps:
        try:
            os.startfile(app["path"])
            time.sleep(1)  # Wait a bit before opening the next app
        except Exception as e:
            messagebox.showerror("Error", f"{app['name']} cannot be opened. The system cannot find the file specified.")

def open_websites():
    websites = [
        "https://www.facebook.com",
        "https://www.chogangroupspa.com",
    ]
    for site in websites:
        try:
            webbrowser.open(site)
            time.sleep(1)  # Wait a bit before opening the next website
        except Exception as e:
            messagebox.showerror("Error", f"Could not open {site}. Error: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    root = tk.Tk()
    root.title("μArch Homelab v0.9.2 (Florina Edition)")
    root.resizable(False, False)
    root.geometry("600x400")

    from PIL import Image, ImageTk
    img_path = os.path.join(base_dir, "homelab.png")
    img = Image.open(img_path)
    img = img.resize((600, 400), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(img)

    background = tk.Label(root, image=bg_image)
    background.place(x=0, y=0, width=600, height=400)

    # keep reference so it isn't garbage collected
    background.image = bg_image

    username = os.getenv("USERNAME")
    label = tk.Label(root, text=f"Welcome back to Homelab, {username}!", bg="#00a2e8")
    label.pack(pady=10)

    open_apps_button = tk.Button(root, text="Open Apps", command=open_apps)
    open_apps_button.pack(pady=10)
    
    open_websites_button = tk.Button(root, text="Open Websites", command=open_websites)
    open_websites_button.pack(pady=10)
    
    root.mainloop()

# Keep the window open
if __name__ == "__main__":
    main()
