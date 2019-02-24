{% for entry in entries %}
<div class="row">
    <ol class="zens">
        <li id="zen-<%= @zen.id %>">
            <span class="title">{{ entry.title }}</span>
            <span class="content">{{ entry.remove_tags_content }}<a href="{{ entry.link }}">show more...</a></span>
            <span class="timestamp">{{ entry.published }}</span>
        </li>
    </ol>
    <br>
</div>
{% endfor %}