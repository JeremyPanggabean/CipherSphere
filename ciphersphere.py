import random
import string
from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from time import sleep
import secrets

console = Console()

# Define character set
CHARS = " " + string.punctuation + string.digits + string.ascii_letters
CHARS = list(CHARS)

class SubstitutionCipher:
    def __init__(self):
        self.chars = CHARS.copy()
        self.key = self.generate_random_key()

    def generate_random_key(self):
        key = self.chars.copy()
        secrets.SystemRandom().shuffle(key)
        return key

    def encrypt(self, plain_text):
        cipher_text = "".join(self.key[self.chars.index(char)] if char in self.chars else char for char in plain_text)
        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = "".join(self.chars[self.key.index(char)] if char in self.key else char for char in cipher_text)
        return plain_text

    def show_key_mapping(self):
        table = Table(title="Character Mapping")
        table.add_column("Original", justify="center", style="cyan")
        table.add_column("Mapped", justify="center", style="magenta")

        for original, mapped in zip(self.chars, self.key):
            table.add_row(original, mapped)

        console.print(table)

    def animated_message(self, message="Processing..."):
        console.print(f":hourglass: [bold cyan]{message}[/bold cyan]", end="")
        sleep(1)
        console.print(" Done! :sparkles:")

if __name__ == "__main__":
    cipher = SubstitutionCipher()

    console.print("[bold cyan]\nWelcome to the Ultra-Modern Command Line Cipher Tool![/bold cyan] :key:")

    while True:
        console.print("\n[bold magenta]=== Substitution Cipher Menu ===[/bold magenta]")
        console.print("[green]1. Encrypt a message[/green]")
        console.print("[yellow]2. Decrypt a message[/yellow]")
        console.print("[magenta]3. Show current key mapping[/magenta]")
        console.print("[blue]4. Generate a new key (Super Secure Shuffle)[/blue]")
        console.print("[red]5. Exit[/red]")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"], default="1")

        if choice == "1":
            text = Prompt.ask("Enter a message to encrypt")
            cipher.animated_message("Encrypting your message....")
            encrypted_message = cipher.encrypt(text)
            console.print(f"[green]Encrypted message:[/green] [bold]{encrypted_message}[/bold]")
        elif choice == "2":
            text = Prompt.ask("Enter a message to decrypt")
            cipher.animated_message("Decrypting your message....")
            decrypted_message = cipher.decrypt(text)
            console.print(f"[yellow]Decrypted message:[/yellow] [bold]{decrypted_message}[/bold]")
        elif choice == "3":
            cipher.show_key_mapping()
        elif choice == "4":
            cipher.key = cipher.generate_random_key()
            cipher.animated_message("Generating a new key")
            console.print("[blue bold]New key generated successfully![/blue bold]")
        elif choice == "5":
            cipher.animated_message("Exiting the program")
            console.print("[bold red]Goodbye! Stay encrypted![/bold red] :wave:")
            break
