import { StyleSheet, Text, View } from 'react-native';
import axios from 'axios';
import { useState, useEffect, useContext } from 'react';
import { AuthContext } from '../store/auth-context';


function WelcomeScreen() {
  const [fetchedMessage, setFetchedMessage] = useState('')
  const authCtx = useContext(AuthContext)
  const token = authCtx.token
  
  useEffect(() => {
    axios.get(
      `http/message.json?auth=${token}`
    ).then(
      response => setFetchedMessage(_ => response.data)
    )
  }, [token])

  return (
    <View style={styles.rootContainer}>
      <Text style={styles.title}>Welcome!</Text>
      <Text>{fetchedMessage}</Text>
    </View>
  );
}

export default WelcomeScreen;

const styles = StyleSheet.create({
  rootContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 32,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8,
  },
});