import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import AllPlaces from './src/screens/AllPlaces';
import AddPlace from './src/screens/AddPlace';
import IconButton from './src/components/UI/IconButton';
import { Colors } from './src/constants/colors';
import Map from './src/screens/Map';
import { init } from './src/util/database';
import { useState, useEffect } from 'react';
import PlaceDetails from './src/screens/PlaceDetails';


const Stack = createNativeStackNavigator()
export default function App() {

  const [appIsReady, setAppIsReady] = useState(false)

  useEffect(() => {
    init()
      .then(_ => {
        setAppIsReady(true)
      })
      .catch(error => console.log(error))
  }, [])

  return (
    <>
      <StatusBar style='dark' />
      <NavigationContainer>
        <Stack.Navigator
          screenOptions={{
            headerStyle: { backgroundColor: Colors.primary500 },
            headerTintColor: Colors.gray700,
            contentStyle: { backgroundColor: Colors.gray700 }
          }}>
          <Stack.Screen name='AllPlaces'
            component={AllPlaces}
            options={({ navigation }) => ({
              headerRight: ({ tintColor }) => <IconButton
                icon='add'
                color={tintColor}
                size={24}
                onPress={() => navigation.navigate('AddPlace')} />,
              title: 'Your favourite places'
            }
            )}
          />
          <Stack.Screen name='AddPlace'
            component={AddPlace}
            options={{
              title: 'Add a new places'
            }}
          />
          <Stack.Screen name="Map" component={Map} />
          <Stack.Screen name="PlaceDetails"
            component={PlaceDetails}
            options={{
              title: 'Loading place'
            }} />
        </Stack.Navigator>
      </NavigationContainer>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
