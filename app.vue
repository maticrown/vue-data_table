<div id="app">
  <Todos/>
</div>

<script>
  import Todos from './components/Todos.vue'

  export default {
  name: 'app',
  components: {
    Todos
    }
  }
</script>

const store = new Vuex.Store({
state: {
  loadingStatus: 'notLoading',
  todos: [{...},{...},{...}]
},
mutations: {
SET_LOADING_STATUS(state,status) {
  state.loadingStatus = status
  },
},
actions: {
fetchTodos(context) {
  context.commit('SET_LOADING_STATUS', 'loading')
  axios.get('api/todos').then(response => {
  context.commit('SET_LOADING_STATUS', 'notLoading')
  context.commit('SET_TODOS',response.data.todos)
      })
    }
  }
})
