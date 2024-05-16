import AuthContent from '../components/auth/AuthContent';
import { useContext, useState } from 'react';
import { login } from '../util/auth';
import LoadingOverlay from '../components/ui/LoadingOverlay';
import { Alert } from 'react-native';
import { AuthContext } from '../store/auth-context';


function LoginScreen() {
  const [isAuthenticating, setIsAuthenticating] = useState(false)
  const authCtx = useContext(AuthContext)

  const loginHandler = async ({ email, password }) => {
    setIsAuthenticating(true)
    try {
      const token = await login(email, password)
      authCtx.authenticate(token)
    } catch (error) {
      Alert.alert(
        'Authentication failed',
        "Couldn't let you in. Check your credentials"
      )
      setIsAuthenticating(false)
    }
    
  }

  if (isAuthenticating) {
    return <LoadingOverlay message='Logging in ...' />
  }
  return <AuthContent isLogin onAuthenticate={loginHandler} />;
}

export default LoginScreen;