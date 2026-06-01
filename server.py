import http.server
import socketserver
import webbrowser
import os

PORT = 8080

# Создаём простой HTTP сервер
Handler = http.server.SimpleHTTPRequestHandler

# Проверяем, есть ли index.html
if not os.path.exists('index.html'):
    print("❌ Ошибка: Файл index.html не найден!")
    print("Создай файл index.html в той же папке")
    exit()

# Запускаем сервер
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n✅ Сервер успешно запущен!")
        print(f"📱 Открой в браузере: http://localhost:{PORT}")
        print(f"🔗 Для Telegram используй ngrok: ngrok http {PORT}")
        print(f"\n⏹️  Для остановки сервера нажми Ctrl+C в этой консоли\n")

        # Автоматически открываем браузер
        webbrowser.open(f'http://localhost:{PORT}')

        # Запускаем сервер
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\n\n👋 Сервер остановлен")
except Exception as e:
    print(f"❌ Ошибка: {e}")
    print("Возможно, порт 8080 уже занят. Попробуй закрыть другие программы")