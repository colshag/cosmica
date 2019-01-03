using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class exitGame : MonoBehaviour
{
    public void exitMyGame()
    {
        Debug.Log("You Pressed the Exit Button");
        Application.Quit();
    }
}
