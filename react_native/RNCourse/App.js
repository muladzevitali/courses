import { useState } from 'react'
import { StyleSheet, TextInput, Text, View, Button, ScrollView, FlatList } from 'react-native';

export default function App() {
  const [enteredGoalText, setEnteredGoalText] = useState('');
  const [courseGoals, setCourseGoals] = useState([]);

  function goalInputHandler(enteredText) {
    setEnteredGoalText(enteredText);
  };

  function addGoalHandler() {
    setCourseGoals(currentCourseGoals => [
      ...currentCourseGoals, 
      {text: enteredGoalText, key: Math.random().toString()}
    ])
  };

  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput
          placeholder="Your goal"
          style={styles.textInput}
          onChangeText={goalInputHandler} />

        <Button title='Add goal' onPress={addGoalHandler} />
      </View>
      <View style={styles.goalsContainer}>
        <FlatList
          alwaysBounceVertical={false}
          data={courseGoals}
          renderItem={itemData => {
            return (
              <View style={styles.goalItemContainer}>
                <Text style={styles.goalItemText}>{itemData.item.text}</Text>
              </View>
            )
          }}
          keyExtractor={(item, _) => item.key}
        />
      </View>
    </View>
  ); s
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    paddingTop: 50,
    paddingHorizontal: 16,

  },
  inputContainer: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 24,
    borderBottomWidth: 2,
    borderBottomColor: '#cccccc'
  },
  textInput: {
    borderWidth: 1,
    width: '70%',
    margin: 8,
    padding: 8
  },
  goalsContainer: {
    flex: 5
  },
  goalItemContainer: {
    flex: 1,
    margin: 8,
    padding: 8,
    borderRadius: 6,
    backgroundColor: '#5e0acc',
  },
  goalItemText: {
    color: 'white'
  }

});
