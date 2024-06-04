# Пересоздание диаграммы без предложенных улучшений, только текущая структура сайта

from graphviz import Digraph

# Создание объекта графа
dot = Digraph(comment='osu.ppy.sh Website Structure')

# Главная страница и её компоненты
dot.node('Home', 'Главная страница')
dot.node('Nav', 'Навигационная панель')
dot.node('Content', 'Основной контент')
dot.node('Footer', 'Футер')

# Добавление связей для главной страницы
dot.edge('Home', 'Nav')
dot.edge('Home', 'Content')
dot.edge('Home', 'Footer')

# Разделы навигационной панели
sections = [
    'Play', 'Community', 'Blog', 'Forums', 'Store', 'About', 'Login'
]
for section in sections:
    dot.node(section, section)
    dot.edge('Nav', section)

# Структура разделов
# Play
dot.node('Download', 'Загрузка игры')
dot.node('Modes', 'Режимы игры')
dot.node('Leaderboards', 'Таблицы лидеров')
dot.edge('Play', 'Download')
dot.edge('Play', 'Modes')
dot.edge('Play', 'Leaderboards')

# Community
dot.node('Users', 'Пользователи')
dot.node('Groups', 'Группы')
dot.node('Events', 'События')
dot.node('Chats', 'Чаты')
dot.edge('Community', 'Users')
dot.edge('Community', 'Groups')
dot.edge('Community', 'Events')
dot.edge('Community', 'Chats')

# Blog
dot.node('Posts', 'Последние записи')
dot.node('Archive', 'Архив')
dot.edge('Blog', 'Posts')
dot.edge('Blog', 'Archive')

# Forums
dot.node('Discussions', 'Общие обсуждения')
dot.node('Support', 'Поддержка')
dot.node('Ideas', 'Предложения и идеи')
dot.edge('Forums', 'Discussions')
dot.edge('Forums', 'Support')
dot.edge('Forums', 'Ideas')

# Store
dot.node('Products', 'Продукты')
dot.node('Cart', 'Корзина')
dot.node('PurchaseHistory', 'История покупок')
dot.edge('Store', 'Products')
dot.edge('Store', 'Cart')
dot.edge('Store', 'PurchaseHistory')

# About
dot.node('History', 'История')
dot.node('Team', 'Команда')
dot.node('Jobs', 'Вакансии')
dot.edge('About', 'History')
dot.edge('About', 'Team')
dot.edge('About', 'Jobs')

# Footer components
dot.node('PrivacyPolicy', 'Политика конфиденциальности')
dot.node('TermsOfUse', 'Условия использования')
dot.node('Contact', 'Контакты')
dot.edge('Footer', 'PrivacyPolicy')
dot.edge('Footer', 'TermsOfUse')
dot.edge('Footer', 'Contact')

# Сохранение диаграммы
dot.format = 'png'
file_path = '/mnt/data/osu_website_structure_no_changes'
dot.render(file_path)

file_path
