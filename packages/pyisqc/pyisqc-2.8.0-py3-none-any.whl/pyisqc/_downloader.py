
import requests
import os 
from rich.progress import Progress, BarColumn, DownloadColumn, TextColumn, TransferSpeedColumn, TimeRemainingColumn



class Downloader:
    @staticmethod
    def downloadSingleFile(url, destPath, filename):
        # Ensure the destination directory exists
        if not os.path.exists(destPath):
            os.makedirs(destPath, exist_ok=True)
        
        # Full path to the file
        file_path = os.path.join(destPath, filename)

        # Stream the response from the URL
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            # No content length header
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            total_length = int(total_length)
            chunk_size = 1024
            num_bars = total_length // chunk_size

            # Setup the progress bar
            with Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                DownloadColumn(),
                TransferSpeedColumn(),
                TimeRemainingColumn(),
            ) as progress:
                task = progress.add_task("Downloading...", total=total_length)

                with open(file_path, 'wb') as f:
                    for data in response.iter_content(chunk_size=chunk_size):
                        f.write(data)
                        progress.update(task, advance=len(data))