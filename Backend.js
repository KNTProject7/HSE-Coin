const express = require('express');
const bodyParser = require('body-parser');
const TelegramBot = require('node-telegram-bot-api');
const fetch = require('node-fetch');

const app = express();
app.use(bodyParser.json());

// Имитируем базу данных
let userScores = {}; // { userId: score }

// Обработчик для сохранения счета
app.post('/save-score', (req, res) => {
    const { userId, score } = req.body; // Получаем userId от клиента
    userScores[userId] = score; // Сохраняем счет для пользователя
    res.json({ status: 'success', score: userScores[userId] });
});

// Обработчик для получения счета
app.get('/get-score/:userId', (req, res) => {
    const userId = req.params.userId;
    const score = userScores[userId] || 0; // Если счета нет, возвращаем 0
    res.json({ score: score });
});

// Настраиваем Telegram-бот
const bot = new TelegramBot('7535373221:AAHcgr-bHLbZVpmrLUV_L6mKnb6DadqJGqw', { polling: true });

// Команда для получения текущего счета через бота
bot.onText(/\/score/, (msg) => {
    const chatId = msg.chat.id;
    const userId = `telegram_${chatId}`; // Используем chatId как идентификатор пользователя

    fetch(`http://localhost:3000/get-score/${userId}`)
        .then(response => response.json())
        .then(data => {
            const score = data.score;
            bot.sendMessage(chatId, `Ваш текущий счет: ${score}`);
        })
        .catch(error => {
            console.error('Ошибка при получении счета:', error);
            bot.sendMessage(chatId, 'Произошла ошибка при получении счета.');
        });
});

// Команда для увеличения счета через бота
bot.onText(/\/click/, (msg) => {
    const chatId = msg.chat.id;
    const userId = `telegram_${chatId}`;

    fetch(`http://localhost:3000/get-score/${userId}`)
        .then(response => response.json())
        .then(data => {
            let score = data.score + 1;

            fetch('http://localhost:3000/save-score', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ userId: userId, score: score })
            }).then(response => response.json())
              .then(data => {
                  bot.sendMessage(chatId, `Ваш новый счет: ${data.score}`);
              })
              .catch(error => {
                  console.error('Ошибка сохранения счета:', error);
                  bot.sendMessage(chatId, 'Ошибка сохранения счета.');
              });
        });
});

app.listen(3000, () => {
    console.log('Сервер запущен на порту 3000');
});
