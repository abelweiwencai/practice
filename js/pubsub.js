var _topics
function subscribe(topics, sender, callback) {
    topics = topic.split('/\s./g');
    for (var i=0, l=topics.length(); i<l; i++) {
        var topic = topics[i]
        if (!_topics.hasProperty(topic)) {
            _topics[topics[i]] = [];
        }

        if (typeof sender === 'function') {
            callback = sender;
            sender = null;
        }

        _topics.push({sender:sender, callback: callback});

    }

    return true;

}

