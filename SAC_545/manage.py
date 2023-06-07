from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-user-stories')
def get_user_stories():
    jira_url = "https://example.com/api/user-stories" # Replace with actual Jira API URL
    response = requests.get(jira_url)
    if response.status_code == 200:
        user_stories = response.json()
        return jsonify(user_stories)
    else:
        return jsonify({'error': 'Unable to fetch user stories from Jira API'})

@app.route('/select-user-story/<int:story_id>')
def select_user_story(story_id):
    jira_url = "https://example.com/api/user-stories/{}".format(story_id) # Replace with actual Jira API URL
    response = requests.get(jira_url)
    if response.status_code == 200:
        user_story = response.json()
        return jsonify(user_story)
    else:
        return jsonify({'error': 'Unable to fetch user story with id {} from Jira API'.format(story_id)})

if __name__ == '__main__':
    app.run(debug=True)