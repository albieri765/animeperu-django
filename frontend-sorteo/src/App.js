import React, { useState } from "react";

function App() {
  const [mensaje, setMensaje] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData(e.target);

    // Cambia la URL si tu backend está en otro dominio al probar local
    const res = await fetch("/sorteo/", {
      method: "POST",
      body: data,
      credentials: "include",
    });

    if (res.redirected || res.ok) {
      setMensaje("🎉 ¡Gracias por participar!");
      e.target.reset();
    } else {
      setMensaje("⛔ Algo salió mal, inténtalo de nuevo.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 to-indigo-700">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 rounded-xl shadow-xl w-full max-w-md space-y-4"
      >
        <h1 className="text-2xl font-bold text-center text-indigo-700">
          Sorteo Anime VIP
        </h1>

        <input
          name="nombre"
          required
          placeholder="Tu nombre"
          className="w-full p-3 border rounded"
        />

        <input
          name="email"
          type="email"
          required
          placeholder="Tu correo"
          className="w-full p-3 border rounded"
        />

        <input
          name="anime_fav"
          placeholder="Anime favorito"
          className="w-full p-3 border rounded"
        />

        <button
          type="submit"
          className="w-full bg-indigo-600 hover:bg-indigo-700 text-white p-3 rounded font-bold transition-transform hover:scale-105"
        >
          ¡Participar!
        </button>

        {mensaje && (
          <p className="text-center font-semibold text-green-600">{mensaje}</p>
        )}
      </form>
    </div>
  );
}

export default App;
