import { useState } from 'react'
import { StyleSheet, View, FlatList, Button, Image } from 'react-native';
import { StatusBar } from 'expo-status-bar';

import GoalItem from './components/GoalItem'
import GoalInput from './components/GoalInput';


export default function App() {
  const [courseGoals, setCourseGoals] = useState([]);
  const [modalIsVisible, setModalIsVisible] = useState(false)

  function addGoalHandler(enteredGoalText) {
    setCourseGoals(currentCourseGoals => [
      ...currentCourseGoals,
      { text: enteredGoalText, id: Math.random().toString() }
    ]);
    setModalIsVisible(false);
  };

  function deleteGoalhandler(id) {
    setCourseGoals(currentCourseGoals => {
      return currentCourseGoals.filter(goal => goal.id !== id)
    })
  }

  function startAddGoalHandler() {
    setModalIsVisible(true)
  }

  function endAddGoalHandler() {
    setModalIsVisible(false)
  };

  return (
    <>
      <StatusBar style='light'/>
      <View style={styles.appContainer}>
        <Button title='Add new goal' color='#a065ec' onPress={startAddGoalHandler} />
        <GoalInput onAddGoal={addGoalHandler} isVisible={modalIsVisible} onCancel={endAddGoalHandler} />
        <View style={styles.goalsContainer}>
          <FlatList
            alwaysBounceVertical={false}
            data={courseGoals}
            renderItem={itemData => {
              return (
                <GoalItem text={itemData.item.text} id={itemData.item.id} onDeleteItem={deleteGoalhandler} />
              )
            }}
            keyExtractor={(item, _) => item.id}
          />
        </View>
      </View>
    </>

  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    paddingTop: 50,
    paddingHorizontal: 16,

  },
  goalsContainer: {
    flex: 5
  }

});
