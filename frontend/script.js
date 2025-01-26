document.addEventListener('DOMContentLoaded', () => {
    const longUrlInput = document.getElementById('long-url');
    const customUrlInput = document.getElementById('custom-url');
    const shortenBtn = document.getElementById('shorten-btn');
    const resultDiv = document.getElementById('result');
    const shortUrlInput = document.getElementById('short-url');
    const copyButton = document.getElementById('copy-button');

    shortenBtn.addEventListener('click', async () => {
        const longUrl = longUrlInput.value.trim();
        const customUrl = customUrlInput.value.trim();

        if (!longUrl) {
            alert('Please enter a long URL.');
            return;
        }

       try {
          const shortUrl = await shortenUrl(longUrl, customUrl);

          if (shortUrl) {
             shortUrlInput.value = shortUrl;
             resultDiv.style.display = 'flex';
            } else {
                alert('Error shortening URL.');
            }
       } catch (error) {
           console.error('Error:', error);
          alert('An error occurred. Please try again.');
        }
    });

    copyButton.addEventListener('click', () => {
        shortUrlInput.select();
        document.execCommand('copy');
    });

     async function shortenUrl(longUrl, customUrl) {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/shorten', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ longUrl, customUrl }),
            });
              if(!response.ok){
                  throw new Error(`HTTP error! Status: ${response.status}`)
                }
            const data = await response.json();
            console.log(data);
            return data.shortUrl
         } catch (error) {
             console.error("Error:", error);
            return null
        }
    }
});