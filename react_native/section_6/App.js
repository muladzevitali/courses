import CategoriesScreen from './src/screens/CategoriesScreen';
import { StatusBar } from 'expo-status-bar';
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import { createDrawerNavigator } from '@react-navigation/drawer'
import { Ionicons } from '@expo/vector-icons'

import MealsOverviewScreen from './src/screens/MealsOverviewScreen';
import MealDetailScreen from './src/screens/MealDetailScreen';
import FavouritesScreen from './src/screens/FavouritesScreen';

const Stack = createStackNavigator()
const Drawer = createDrawerNavigator()


const DrawerNavigator = () => {
  return (
    <Drawer.Navigator
      screenOptions={{
        headerStyle: { backgroundColor: '#351401' },
        headerTintColor: 'white',
        sceneContainerStyle: { backgroundColor: '#3f2f25' },
        drawerContentStyle: { backgroundColor: '#351401' },
        drawerInactiveTintColor: 'white',
        drawerActiveTintColor: '#351401',
        drawerActiveBackgroundColor: '#e4baa1'
      }}
    >
      <Drawer.Screen
        name="Categories"
        component={CategoriesScreen}
        options={{
          title: 'All Categories',
          drawerIcon: ({ color, size }) => <Ionicons color={color} size={size} name='list' />
        }}
      />
      <Drawer.Screen
        name="Favourites"
        component={FavouritesScreen} 
        options={{
          title: 'Favourites',
          drawerIcon: ({ color, size }) => <Ionicons color={color} size={size} name='star' />
        }}
        />
    </Drawer.Navigator>
  )
}

export default function App() {
  return (
    <>
      <StatusBar style='light' />
      <NavigationContainer>
        <Stack.Navigator
          initialRouteName='MealCategoeries'
          screenOptions={{
            headerStyle: { backgroundColor: '#351401' },
            headerTintColor: 'white',
            sceneContainerStyle: { backgroundColor: '#3f2f25' }
          }}
        >
          <Stack.Screen
            name='Drawer'
            // component={CategoriesScreen}
            component={DrawerNavigator}
            options={{
              headerShown: false

            }}
          />
          <Stack.Screen
            name='MealsOverview'
            component={MealsOverviewScreen}
          />
          <Stack.Screen
            name='MealDetail'
            component={MealDetailScreen}
            options={{
              title: 'About the Meal'
            }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </>
  );
}
