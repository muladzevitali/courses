import { StatusBar } from 'expo-status-bar';
import { StyleSheet, ImageBackground, SafeAreaView } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient'
import { useFonts } from 'expo-font';
import AppLoading from 'expo-splash-screen'
import { useState } from 'react';

import GameScreen from './src/screens/GameScreen';
import StartGameScreen from './src/screens/StartGameScreen';
import GameOverScreen from './src/screens/GameOverScreen';
import Colors from './src/constants/colors';

export default function App() {
  const [enteredNumber, setEnteredNumber] = useState(null)
  const [gameIsOver, setGameIsOver] = useState(false)
  const [numberOfRounds, setNumberOfRounds] = useState(0)

  const [fontsLoaded] = useFonts({
    'open-sans': require('./assets/fonts/OpenSans-Regular.ttf'),
    'open-sans-bold': require('./assets/fonts/OpenSans-Bold.ttf')
  })

  const enteredNumberHandler = (number) => {
    setEnteredNumber(_ => number)
    setGameIsOver(false)
  }

  const gameOverHandler = (numberOfRounds) => {
    setGameIsOver(_ => true)
    setNumberOfRounds(_ => numberOfRounds)
  }

  const startNewGameHandler = () => {
    setEnteredNumber(_ => null);
    setNumberOfRounds(_ => 0)
  }

  let screen = <StartGameScreen onEnterNumber={enteredNumberHandler} />


  if (enteredNumber) {
    screen = <GameScreen enteredNumber={enteredNumber} onGameOver={gameOverHandler} />
  }

  if (gameIsOver && enteredNumber) {
    screen = <GameOverScreen enteredNumber={enteredNumber} numberOfRounds={numberOfRounds} onRestart={startNewGameHandler} />
  }

  // if (!fontsLoaded) {
  //   return <AppLoading />
  // }

  return (
    <>
      <StatusBar style="auto" />
      <LinearGradient colors={[Colors.primary700, Colors.accent500]} style={styles.rootScreen}>
        <ImageBackground
          source={require('./assets/images/background.png')}
          resizeMode='cover'
          style={styles.rootScreen}
          imageStyle={styles.backgroundImage}
        >
          <SafeAreaView style={styles.rootScreen}>
            {screen}
          </SafeAreaView>

        </ImageBackground>
      </LinearGradient>
    </>
  );
}

const styles = StyleSheet.create({
  rootScreen: {
    flex: 1
  },
  backgroundImage: {
    opacity: .15
  }
});
