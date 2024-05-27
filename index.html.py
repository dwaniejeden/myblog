<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Osobisty Blog</title>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans&family=Roboto:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Open Sans', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 1rem;
            text-align: center;
        }
        header h1 {
            font-family: 'Roboto', sans-serif;
            margin: 0;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #444;
        }
        nav a {
            color: #fff;
            padding: 1rem;
            text-decoration: none;
        }
        nav a:hover {
            background-color: #555;
        }
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 1rem;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .post img, .post audio {
            max-width: 100%;
            display: block;
            margin: 1rem 0;
        }
        footer {
            text-align: center;
            padding: 1rem;
            background-color: #333;
            color: #fff;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        .form-group label {
            display: block;
            margin-bottom: .5rem;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: .5rem;
            box-sizing: border-box;
        }
        .form-group input[type="file"] {
            padding: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Osobisty Blog</h1>
    </header>
    <nav>
        <a href="#home">Blog</a>
        <a href="#biografia">Biografia</a>
        <a href="#kontakt">Kontakt</a>
    </nav>
    <div class="container" id="home">
        <h2>Najnowsze wpisy</h2>
        <div id="posts">
            <div class="post">
                <h3>Tytuł wpisu</h3>
                <p>Treść wpisu. To jest przykładowy wpis na blogu.</p>
                <img src="przyklad.jpg" alt="Przykładowe zdjęcie">
                <audio controls>
                    <source src="przyklad.mp3" type="audio/mpeg">
                    Twoja przeglądarka nie obsługuje elementu audio.
                </audio>
            </div>
        </div>
    </div>
    <div class="container" id="biografia">
        <h2>Biografia</h2>
        <p>Twoja biografia. Tu możesz umieścić informacje o sobie.</p>
    </div>
    <div class="container" id="kontakt">
        <h2>Kontakt</h2>
        <form action="#" method="post">
            <div class="form-group">
                <label for="name">Imię:</label>
                <input type="text" id="name" name="name">
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email">
            </div>
            <div class="form-group">
                <label for="message">Wiadomość:</label>
                <textarea id="message" name="message"></textarea>
            </div>
            <input type="submit" value="Wyślij">
        </form>
    </div>
    <div class="container">
        <h2>Dodaj nowy wpis</h2>
        <form id="newPostForm">
            <div class="form-group">
                <label for="postTitle">Tytuł wpisu:</label>
                <input type="text" id="postTitle" name="postTitle" required>
            </div>
            <div class="form-group">
                <label for="postContent">Treść wpisu:</label>
                <textarea id="postContent" name="postContent" required></textarea>
            </div>
            <div class="form-group">
                <label for="postImage">Zdjęcie:</label>
                <input type="file" id="postImage" name="postImage" accept="image/*">
            </div>
            <div class="form-group">
                <label for="postAudio">Utwór muzyczny:</label>
                <input type="file" id="postAudio" name="postAudio" accept="audio/*">
            </div>
            <input type="submit" value="Dodaj wpis">
        </form>
    </div>
    <footer>
        <p>&copy; 2024 Twoje Imię. Wszelkie prawa zastrzeżone.</p>
    </footer>
    <script>
        document.getElementById('newPostForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const title = document.getElementById('postTitle').value;
            const content = document.getElementById('postContent').value;
            const imageFile = document.getElementById('postImage').files[0];
            const audioFile = document.getElementById('postAudio').files[0];

            const postContainer = document.createElement('div');
            postContainer.classList.add('post');

            const postTitle = document.createElement('h3');
            postTitle.textContent = title;
            postContainer.appendChild(postTitle);

            const postContent = document.createElement('p');
            postContent.textContent = content;
            postContainer.appendChild(postContent);

            if (imageFile) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    postContainer.appendChild(img);
                }
                reader.readAsDataURL(imageFile);
            }

            if (audioFile) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const audio = document.createElement('audio');
                    audio.controls = true;
                    const source = document.createElement('source');
                    source.src = e.target.result;
                    source.type = audioFile.type;
                    audio.appendChild(source);
                    postContainer.appendChild(audio);
                }
                reader.readAsDataURL(audioFile);
            }

            document.getElementById('posts').appendChild(postContainer);
            document.getElementById('newPostForm').reset();
        });
    </script>
</body>
</html>