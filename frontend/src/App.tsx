import React, {useState} from 'react';
import logo from './logo.svg';
import emf_logo from './img/petites_recettes_black_font_logo.png'
import './App.css';
import Navbar from './components/Navbar/Navbar';
import IngredientsPicker from './components/IngredientsPicker/IngredientsPicker';
import RecipeFinder from './components/RecipeFinder/RecipeFinder';

interface Ingredient {
  name: string,
  quantity: number
}

function App() {

  const [ingredients, setIngredients] = useState<Ingredient[]>([])

  return (
    <div className="App">
      <Navbar></Navbar>
      <div className='main-content'>
        <span className="IngredientsPicker">
          <IngredientsPicker></IngredientsPicker>
        </span>
        
        <span className="RecipeFinder">
          <RecipeFinder></RecipeFinder>
        </span>
      </div>
      
    </div>
  );
}

export default App;
