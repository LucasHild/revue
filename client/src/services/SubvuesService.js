import Api from '@/services/Api'

export default {
  item(permalink) {
    return Api().get('subvues/' + permalink)
  },

  create(post) {
    return Api().post('subvues', post)
  },

  posts(permalink) {
    return Api().get('subvues/' + permalink + '/posts')
  }
}
