import Api from '@/services/Api'

export default {
  index() {
    return Api().get('posts')
  },

  create(post) {
    return Api().post('posts', post)
  },

  delete(id) {
    return Api().delete('posts/id/' + id)
  },

  item(id) {
    return Api().get('posts/id/' + id)
  },

  user(username) {
    return Api().get('posts/user/' + username)
  },

  addComment(postId, commentContent) {
    return Api().post('posts/' + postId + '/comments', { content: commentContent })
  },

  upVote(postId) {
    return Api().post('posts/' + postId + '/upvote')
  },

  downVote(postId) {
    return Api().post('posts/' + postId + '/downvote')
  }
}
