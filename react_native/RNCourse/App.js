import { StyleSheet, Text, View, Button } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View>
      <Text>mariam miyvarxar</Text>
      </View>
      <Text>Hello World!</Text>
      <Button title="გაგზავნა"/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#599e46',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
