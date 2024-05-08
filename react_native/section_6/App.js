import CategoriesScreen from './src/screens/CategoriesScreen';
import { StatusBar } from 'expo-status-bar';
import { NavigationContainer } from '@react-navigation/native'
import { Button } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack'
import MealsOverviewScreen from './src/screens/MealsOverviewScreen';
import { CATEGORIES } from './data/dummy-data';
import MealDetailScreen from './src/screens/MealDetailScreen';

const Stack = createStackNavigator()

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
            contentStyle: { backgroundColor: '#3f2f25' }
          }}
        >
          <Stack.Screen
            name='MealCategoeries'
            component={CategoriesScreen}
            options={{
              title: 'All Categories',

            }}
          />
          <Stack.Screen
            name='MealsOverview'
            component={MealsOverviewScreen}
          // options={({route, navigation}) => {
          //   const categoryId = route.params.categoryId;
          //   const category = CATEGORIES.filter()
          //   return {
          //     title: categoryId
          //   }
          // }}
          />
          <Stack.Screen
            name='MealDetail'
            component={MealDetailScreen}
          />
        </Stack.Navigator>

      </NavigationContainer>
    </>
  );
}
