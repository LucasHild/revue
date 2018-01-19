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
  }
}
