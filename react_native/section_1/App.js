import { useState } from 'react';
import { StyleSheet, View, FlatList, Button } from 'react-native';
import GoalItem from './src/components/GoalItem';
import GoalInput from './src/components/GoalInput';
import { StatusBar } from 'expo-status-bar';


export default function App() {
  const [goals, setGoals] = useState([])
  const [modalIsVisible, setModalIsVisible] = useState(false)

  const addGoalHandler = (enteredGoalText) => {
    setGoals(prevGoals => [{ text: enteredGoalText, id: Math.random().toString() }, ...prevGoals])
    endAddGoalHandler()
  }

  const deleteGoalHandler = (itemId) => {
    setGoals(currentGoals => currentGoals.filter(item => item.id !== itemId))
  }

  const startAddGoalHandler = () => {
    setModalIsVisible(true)
  }

  const endAddGoalHandler = () => {
    setModalIsVisible(false)
  }

  return (
    <>
      <StatusBar style='light'/>
      <View style={styles.appContainer}>
        <Button title="Add New Goal" color="#5e0acc" onPress={startAddGoalHandler} />
        <GoalInput onAddGoal={addGoalHandler} endCancelGoal={endAddGoalHandler} visible={modalIsVisible} />
        <View style={styles.goalsContainer}>
          <FlatList
            alwaysBounceVertical={false}
            data={goals}
            renderItem={(itemData) => <GoalItem goalItemData={itemData.item} onDeleteItem={deleteGoalHandler} />}
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
    paddingHorizontal: 16
  },
  goalsContainer: {
    flex: 4,
    paddingTop: 10
  }
});
