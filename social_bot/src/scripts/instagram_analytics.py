from textblob import TextBlob


def gather_instagram_analytics(bot, username):
    try:
        print("Starting analytics...")

        # Get user posts
        print("Getting user's posts...")
        user_id = bot.get_user_id_from_username(username)
        recent_posts = bot.get_user_medias(user_id, filtration=False)

        # Sort posts by engagement (likes + comments)
        print("Sorting posts...")
        top_posts = sorted(recent_posts, key=lambda post: bot.get_media_info(post)[0]['like_count'] + bot.get_media_info(post)[0]['comment_count'], reverse=True)[:10]

        print(f'"{username}" top posts:')

        # Analyze sentiment of comments in each post
        for index, post in enumerate(top_posts, start=1):
            comments = bot.get_media_comments_all(post)
            sentiments = [TextBlob(comment['text']).sentiment.polarity for comment in comments]
            average_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
            
            post_info = bot.get_media_info(post)[0]
            post_url = f"https://www.instagram.com/p/{post_info['code']}/"
            
            print(f"Post {index}: {post_url}")
            print(f"   Likes: {post_info['like_count']}")
            print(f"   Average sentiment: {average_sentiment}")
    except Exception as e:
        print(f"Error during analytics: {e}")
