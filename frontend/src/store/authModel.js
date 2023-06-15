// export const autModel = {
//     state: () => ({
//         token: '',
//         isAuthenticated: false,
//     }),
//
//     mutations: {
//         initializeStore(state) {
//             if (localStorage.getItem('token')) {
//                 state.token = localStorage.getItem('token')
//                 state.isAuthenticated = true
//             } else {
//                 state.token = ''
//                 state.isAuthenticated = false
//             }
//         },
//         setToken(state, token) {
//             state.token = token
//             state.isAuthenticated = false
//         },
//         removeToken(state, token) {
//             state.token = ''
//             state.isAuthenticated = false
//         }
//     },
//     actions: {
//
//     },
//     namespaced: true,
//
// }