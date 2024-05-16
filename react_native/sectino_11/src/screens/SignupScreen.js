import { useContext, useState } from 'react';
import AuthContent from '../components/auth/AuthContent';
import { createUser } from '../util/auth';
import LoadingOverlay from '../components/ui/LoadingOverlay';
import { Alert } from 'react-native';
import { AuthContext } from '../store/auth-context';

function SignupScreen() {

  const [isAuthenticating, setIsAuthenticating] = useState(false)
  const authCtx = useContext(AuthContext)

  const signUpHandler = async ({ email, password }) => {
    setIsAuthenticating(true)
    try {
      const token = await createUser(email, password)
      authCtx.authenticate(token)
    } catch (error) {
      Alert.alert(
        'Failed to register',
        "Couldn't register user with given credentials"
      )
    }

    setIsAuthenticating(false)
  }
  if (isAuthenticating) {
    return <LoadingOverlay message='Registering user ...' />
  }

  return <AuthContent onAuthenticate={signUpHandler} />;
}


export default SignupScreen;