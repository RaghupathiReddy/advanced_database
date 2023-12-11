<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Accounts</a></li>
            <li><a href="/contacts">Contacts</a></li>
        </ul>
    </nav>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>