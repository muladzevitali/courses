import AsyncStorage from "@react-native-async-storage/async-storage";

import { createContext, useEffect, useState } from "react";

export const AuthContext = createContext({
    token: '',
    isAuthenticated: false,
    authenticate: () => { },
    logout: () => { }
})


const AuthContextProvider = ({ children }) => {
    const [authToken, setAuthToken] = useState()

    const authenticate = (token) => {
        setAuthToken(_ => token)
        AsyncStorage.setItem('token', token)
    }

    const logout = () => {

        setAuthToken(_ => null)
    }

    const value = {
        token: authToken,
        isAuthenticated: !!authToken,
        authenticate: authenticate,
        logout: logout
    }

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthContextProvider