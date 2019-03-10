{% for entry in entries %}
<div class="row">
    <ol class="zens">
        <li id="zen-<%= @zen.id %>">
            <span class="title">{{ entry.name }}</span>
            <span class="content">{{ entry.short_description }}<a href="{{ entry.html_url }}"> ... show more</a></span>
            <span class="timestamp">{{ entry.language }}</span>
            <span class="timestamp">{{ entry.updated_at }}</span>
        </li>
    </ol>
    <br>
</div>
{% endfor %}