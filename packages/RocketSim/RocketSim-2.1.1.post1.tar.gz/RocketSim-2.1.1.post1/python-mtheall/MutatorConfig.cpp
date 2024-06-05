#include "Module.h"

#include "Array.h"

#include <cstring>
#include <type_traits>

namespace RocketSim::Python
{
PyTypeObject *MutatorConfig::Type = nullptr;

PyMemberDef MutatorConfig::Members[] = {
    {.name      = "ball_drag",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballDrag)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballDrag),
        .flags  = 0,
        .doc    = "Ball drag"},
    {.name      = "ball_hit_extra_force_scale",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballHitExtraForceScale)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballHitExtraForceScale),
        .flags  = 0,
        .doc    = "Ball hit extra force scale"},
    {.name      = "ball_mass",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballMass)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballMass),
        .flags  = 0,
        .doc    = "Ball mass"},
    {.name      = "ball_max_speed",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballMaxSpeed)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballMaxSpeed),
        .flags  = 0,
        .doc    = "Ball max speed"},
    {.name      = "ball_radius",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballRadius)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballRadius),
        .flags  = 0,
        .doc    = "Ball radius"},
    {.name      = "ball_world_friction",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballWorldFriction)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballWorldFriction),
        .flags  = 0,
        .doc    = "Ball world friction"},
    {.name      = "ball_world_restitution",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::ballWorldRestitution)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, ballWorldRestitution),
        .flags  = 0,
        .doc    = "Ball world restitution"},
    {.name      = "boost_accel",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::boostAccel)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, boostAccel),
        .flags  = 0,
        .doc    = "Boost accel"},
    {.name      = "boost_pad_cooldown_big",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::boostPadCooldown_Big)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, boostPadCooldown_Big),
        .flags  = 0,
        .doc    = "Boost pad cooldown big"},
    {.name      = "boost_pad_cooldown_small",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::boostPadCooldown_Small)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, boostPadCooldown_Small),
        .flags  = 0,
        .doc    = "Boost pad cooldown small"},
    {.name      = "boost_used_per_second",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::boostUsedPerSecond)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, boostUsedPerSecond),
        .flags  = 0,
        .doc    = "Boost used per second"},
    {.name      = "bump_cooldown_time",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::bumpCooldownTime)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, bumpCooldownTime),
        .flags  = 0,
        .doc    = "Bump cooldown time"},
    {.name      = "bump_force_scale",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::bumpForceScale)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, bumpForceScale),
        .flags  = 0,
        .doc    = "Bump force scale"},
    {.name      = "car_mass",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::carMass)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, carMass),
        .flags  = 0,
        .doc    = "Car mass"},
    {.name      = "car_spawn_boost_amount",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::carSpawnBoostAmount)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, carSpawnBoostAmount),
        .flags  = 0,
        .doc    = "Car spawn boost amount"},
    {.name      = "car_world_friction",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::carWorldFriction)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, carWorldFriction),
        .flags  = 0,
        .doc    = "Car world friction"},
    {.name      = "car_world_restitution",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::carWorldRestitution)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, carWorldRestitution),
        .flags  = 0,
        .doc    = "Car world restitution"},
    {.name      = "unlimited_flips",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::unlimitedFlips)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, unlimitedFlips),
        .flags  = 0,
        .doc    = "Enable unlimited flips"},
    {.name      = "unlimited_double_jumps",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::unlimitedDoubleJumps)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, unlimitedDoubleJumps),
        .flags  = 0,
        .doc    = "Enable unlimited double jumps"},
    {.name      = "demo_mode",
        .type   = TypeHelper<std::underlying_type_t<decltype (RocketSim::MutatorConfig::demoMode)>>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, demoMode),
        .flags  = 0,
        .doc    = "Demo mode"},
    {.name      = "enable_team_demos",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::enableTeamDemos)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, enableTeamDemos),
        .flags  = 0,
        .doc    = "Enable team demos"},
    {.name      = "jump_accel",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::jumpAccel)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, jumpAccel),
        .flags  = 0,
        .doc    = "Jump acceleration"},
    {.name      = "jump_immediate_force",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::jumpImmediateForce)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, jumpImmediateForce),
        .flags  = 0,
        .doc    = "Jump immediate force"},
    {.name      = "respawn_delay",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::respawnDelay)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, respawnDelay),
        .flags  = 0,
        .doc    = "Respawn delay"},
    {.name      = "enable_car_car_collision",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::enableCarCarCollision)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, enableCarCarCollision),
        .flags  = 0,
        .doc    = "Enable car-car collision"},
    {.name      = "enable_car_ball_collision",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::enableCarBallCollision)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, enableCarBallCollision),
        .flags  = 0,
        .doc    = "Enable car-ball collision"},
    {.name      = "goal_base_threshold_y",
        .type   = TypeHelper<decltype (RocketSim::MutatorConfig::goalBaseThresholdY)>::type,
        .offset = offsetof (MutatorConfig, config) + offsetof (RocketSim::MutatorConfig, goalBaseThresholdY),
        .flags  = 0,
        .doc    = "Goal threshold for soccar"},
    {.name = nullptr, .type = 0, .offset = 0, .flags = 0, .doc = nullptr},
};

PyMethodDef MutatorConfig::Methods[] = {
    {.ml_name     = "__getstate__",
        .ml_meth  = (PyCFunction)&MutatorConfig::Pickle,
        .ml_flags = METH_NOARGS,
        .ml_doc   = nullptr},
    {.ml_name     = "__setstate__",
        .ml_meth  = (PyCFunction)&MutatorConfig::Unpickle,
        .ml_flags = METH_O,
        .ml_doc   = nullptr},
    {.ml_name     = "__copy__",
        .ml_meth  = (PyCFunction)&MutatorConfig::Copy,
        .ml_flags = METH_NOARGS,
        .ml_doc   = R"(__copy__(self) -> RocketSim.MutatorConfig
Shallow copy)"},
    {.ml_name     = "__deepcopy__",
        .ml_meth  = (PyCFunction)&MutatorConfig::DeepCopy,
        .ml_flags = METH_O,
        .ml_doc   = R"(__deepcopy__(self, memo) -> RocketSim.MutatorConfig
Deep copy)"},
    {.ml_name = nullptr, .ml_meth = nullptr, .ml_flags = 0, .ml_doc = nullptr},
};

PyGetSetDef MutatorConfig::GetSet[] = {
    GETSET_ENTRY (MutatorConfig, gravity, "Gravity"),
    {.name = nullptr, .get = nullptr, .set = nullptr, .doc = nullptr, .closure = nullptr},
};

PyType_Slot MutatorConfig::Slots[] = {
    {Py_tp_new, (void *)&MutatorConfig::New},
    {Py_tp_init, (void *)&MutatorConfig::Init},
    {Py_tp_dealloc, (void *)&MutatorConfig::Dealloc},
    {Py_tp_members, &MutatorConfig::Members},
    {Py_tp_methods, &MutatorConfig::Methods},
    {Py_tp_getset, &MutatorConfig::GetSet},
    {Py_tp_doc, (void *)R"(Mutator config
__init__(self,
	game_mode: RocketSim.GameMode = RocketSim.GameMode.SOCCAR,
	gravity: RocketSim.Vec = RocketSim.Vec(z = -650.0),
	car_mass: float = 180.0,
	car_world_friction: float = 0.3,
	car_world_restitution: float = 0.3,
	ball_mass: float = <dependent on game_mode>,
	ball_max_speed: float = 6000.0,
	ball_drag: float = 0.03,
	ball_world_friction: float = <dependent on game_mode>,
	ball_world_restitution: float = <dependent on game_mode>,
	jump_accel: float = 4375.0 / 3.0,
	jump_immediate_force: float = 875.0 / 3.0,
	boost_accel: float = 21.2,
	boost_used_per_second: float = 100.0 / 3.0,
	respawn_delay: float = 3.0,
	bump_cooldown_time: float = 0.25,
	boost_pad_cooldown_big: float = 10.0,
	boost_pad_cooldown_small: float = 4.0,
	car_spawn_boost_amount: float = 100.0 / 3.0,
	ball_hit_extra_force_scale: float = 1.0,
	bump_force_scale: float = 1.0,
	ball_radius: float = <dependent on game_mode>,
	unlimited_flips: bool = False,
	unlimited_double_jumps: bool = False,
	demo_mode: int = RocketSim.DemoMode.NORMAL,
	enable_team_demos: bool = False,
	enable_car_car_collision: bool = True,
	enable_car_ball_collision: bool = True),
	goal_base_threshold_y: float = 5124.25))"},
    {0, nullptr},
};

PyType_Spec MutatorConfig::Spec = {
    .name      = "RocketSim.MutatorConfig",
    .basicsize = sizeof (MutatorConfig),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = MutatorConfig::Slots,
};

PyRef<MutatorConfig> MutatorConfig::NewFromMutatorConfig (RocketSim::MutatorConfig const &config_) noexcept
{
	auto const self = PyRef<MutatorConfig>::stealObject (MutatorConfig::New (MutatorConfig::Type, nullptr, nullptr));
	if (!self || !InitFromMutatorConfig (self.borrow (), config_))
		return nullptr;

	return self;
}

bool MutatorConfig::InitFromMutatorConfig (MutatorConfig *const self_, RocketSim::MutatorConfig const &config_) noexcept
{
	auto const gravity = Vec::NewFromVec (config_.gravity);

	if (!gravity)
		return false;

	PyRef<Vec>::assign (self_->gravity, gravity.borrowObject ());

	self_->config = config_;
	return true;
}

RocketSim::MutatorConfig MutatorConfig::ToMutatorConfig (MutatorConfig *self_) noexcept
{
	auto config = self_->config;

	config.gravity = Vec::ToVec (self_->gravity);

	return config;
}

PyObject *MutatorConfig::New (PyTypeObject *subtype_, PyObject *args_, PyObject *kwds_) noexcept
{
	auto const tp_alloc = (allocfunc)PyType_GetSlot (subtype_, Py_tp_alloc);

	auto self = PyRef<MutatorConfig>::stealObject (tp_alloc (subtype_, 0));
	if (!self)
		return nullptr;

	new (&self->config) RocketSim::MutatorConfig{RocketSim::GameMode::SOCCAR};
	self->gravity = nullptr;

	return self.giftObject ();
}

int MutatorConfig::Init (MutatorConfig *self_, PyObject *args_, PyObject *kwds_) noexcept
{
	static char gameModeKwd[]               = "game_mode";
	static char gravityKwd[]                = "gravity";
	static char carMassKwd[]                = "car_mass";
	static char carWorldFrictionKwd[]       = "car_world_friction";
	static char carWorldRestitutionKwd[]    = "car_world_restitution";
	static char ballMassKwd[]               = "ball_mass";
	static char ballMaxSpeedKwd[]           = "ball_max_speed";
	static char ballDragKwd[]               = "ball_drag";
	static char ballWorldFrictionKwd[]      = "ball_world_friction";
	static char ballWorldRestitutionKwd[]   = "ball_world_restitution";
	static char jumpAccelKwd[]              = "jump_accel";
	static char jumpImmediateForceKwd[]     = "jump_immediate_force";
	static char boostAccelKwd[]             = "boost_accel";
	static char boostUsedPerSecondKwd[]     = "boost_used_per_second";
	static char respawnDelayKwd[]           = "respawn_delay";
	static char bumpCooldownTimeKwd[]       = "bump_cooldown_time";
	static char boostPadCooldownBigKwd[]    = "boost_pad_cooldown_big";
	static char boostPadCooldownSmallKwd[]  = "boost_pad_cooldown_small";
	static char carSpawnBoostAmountKwd[]    = "car_spawn_boost_amount";
	static char ballHitExtraForceScaleKwd[] = "ball_hit_extra_force_scale";
	static char bumpForceScaleKwd[]         = "bump_force_scale";
	static char ballRadiusKwd[]             = "ball_radius";
	static char unlimitedFlipsKwd[]         = "unlimited_flips";
	static char unlimitedDoubleJumpsKwd[]   = "unlimited_double_jumps";
	static char demoModeKwd[]               = "demo_mode";
	static char enableTeamDemosKwd[]        = "enable_team_demos";
	static char enableCarCarCollisionKwd[]  = "enable_car_car_collision";
	static char enableCarBallCollisionKwd[] = "enable_car_ball_collision";
	static char goalBaseThresholdYKwd[]     = "goal_base_threshold_y";

	static char *dict[] = {gameModeKwd,
	    gravityKwd,
	    carMassKwd,
	    carWorldFrictionKwd,
	    carWorldRestitutionKwd,
	    ballMassKwd,
	    ballMaxSpeedKwd,
	    ballDragKwd,
	    ballWorldFrictionKwd,
	    ballWorldRestitutionKwd,
	    jumpAccelKwd,
	    jumpImmediateForceKwd,
	    boostAccelKwd,
	    boostUsedPerSecondKwd,
	    respawnDelayKwd,
	    bumpCooldownTimeKwd,
	    boostPadCooldownBigKwd,
	    boostPadCooldownSmallKwd,
	    carSpawnBoostAmountKwd,
	    ballHitExtraForceScaleKwd,
	    bumpForceScaleKwd,
	    ballRadiusKwd,
	    unlimitedFlipsKwd,
	    unlimitedDoubleJumpsKwd,
	    demoModeKwd,
	    enableTeamDemosKwd,
	    enableCarCarCollisionKwd,
	    enableCarBallCollisionKwd,
	    goalBaseThresholdYKwd,
	    nullptr};

	int gameMode = static_cast<int> (RocketSim::GameMode::SOCCAR);

	// first pass to get game mode, second pass to fill in if not
	for (int i = 0; i < 2; ++i)
	{
		switch (static_cast<RocketSim::GameMode> (gameMode))
		{
		case RocketSim::GameMode::SOCCAR:
		case RocketSim::GameMode::HOOPS:
		case RocketSim::GameMode::HEATSEEKER:
		case RocketSim::GameMode::SNOWDAY:
		case RocketSim::GameMode::THE_VOID:
			break;

		default:
			PyErr_Format (PyExc_ValueError, "Invalid game mode '%d'", gameMode);
			return -1;
		}

		RocketSim::MutatorConfig config{static_cast<RocketSim::GameMode> (gameMode)};

		PyObject *gravity = nullptr; // borrowed reference
		int demoMode      = static_cast<int> (config.demoMode);

		int unlimitedFlips         = config.unlimitedFlips;
		int unlimitedDoubleJumps   = config.unlimitedDoubleJumps;
		int enableTeamDemos        = config.enableTeamDemos;
		int enableCarCarCollision  = config.enableCarCarCollision;
		int enableCarBallCollision = config.enableCarBallCollision;

		if (!PyArg_ParseTupleAndKeywords (args_,
		        kwds_,
		        "|iO!ffffffffffffffffffffppipppf",
		        dict,
		        &gameMode,
		        Vec::Type,
		        &gravity,
		        &config.carMass,
		        &config.carWorldFriction,
		        &config.carWorldRestitution,
		        &config.ballMass,
		        &config.ballMaxSpeed,
		        &config.ballDrag,
		        &config.ballWorldFriction,
		        &config.ballWorldRestitution,
		        &config.jumpAccel,
		        &config.jumpImmediateForce,
		        &config.boostAccel,
		        &config.boostUsedPerSecond,
		        &config.respawnDelay,
		        &config.bumpCooldownTime,
		        &config.boostPadCooldown_Big,
		        &config.boostPadCooldown_Small,
		        &config.carSpawnBoostAmount,
		        &config.ballHitExtraForceScale,
		        &config.bumpForceScale,
		        &config.ballRadius,
		        &unlimitedFlips,
		        &unlimitedDoubleJumps,
		        &demoMode,
		        &enableTeamDemos,
		        &enableCarCarCollision,
		        &enableCarBallCollision,
		        &config.goalBaseThresholdY))
			return -1;

		// try again with parsed game mode
		if (i == 0 && static_cast<RocketSim::GameMode> (gameMode) != RocketSim::GameMode::SOCCAR)
			continue;

		config.demoMode = static_cast<RocketSim::DemoMode> (demoMode);

		switch (config.demoMode)
		{
		case RocketSim::DemoMode::NORMAL:
		case RocketSim::DemoMode::ON_CONTACT:
		case RocketSim::DemoMode::DISABLED:
			break;

		default:
			PyErr_Format (PyExc_ValueError, "Invalid demo mode '%d'", demoMode);
			return -1;
		}

		if (gravity)
			config.gravity = Vec::ToVec (PyCast<Vec> (gravity));

		config.unlimitedFlips         = unlimitedFlips;
		config.unlimitedDoubleJumps   = unlimitedDoubleJumps;
		config.enableTeamDemos        = enableTeamDemos;
		config.enableCarCarCollision  = enableCarCarCollision;
		config.enableCarBallCollision = enableCarBallCollision;

		if (!InitFromMutatorConfig (self_, config))
			return -1;

		return 0;
	}

#ifdef __GNUC__
	__builtin_unreachable ();
#elif defined(_MSC_VER)
	__assume (false);
#else
	std::abort ();
#endif
}

void MutatorConfig::Dealloc (MutatorConfig *self_) noexcept
{
	self_->config.~MutatorConfig ();

	Py_XDECREF (self_->gravity);

	auto const tp_free = (freefunc)PyType_GetSlot (Type, Py_tp_free);
	tp_free (self_);
}

PyObject *MutatorConfig::Pickle (MutatorConfig *self_) noexcept
{
	auto dict = PyObjectRef::steal (PyDict_New ());
	if (!dict)
		return nullptr;

	RocketSim::MutatorConfig const model{RocketSim::GameMode::SOCCAR};
	auto const config = ToMutatorConfig (self_);

	if (config.gravity != model.gravity && !DictSetValue (dict.borrow (), "gravity", PyNewRef (self_->gravity)))
		return nullptr;

	if (config.carMass != model.carMass &&
	    !DictSetValue (dict.borrow (), "car_mass", PyFloat_FromDouble (config.carMass)))
		return nullptr;

	if (config.carWorldFriction != model.carWorldFriction &&
	    !DictSetValue (dict.borrow (), "car_world_friction", PyFloat_FromDouble (config.carWorldFriction)))
		return nullptr;

	if (config.carWorldRestitution != model.carWorldRestitution &&
	    !DictSetValue (dict.borrow (), "car_world_restitution", PyFloat_FromDouble (config.carWorldRestitution)))
		return nullptr;

	if (config.ballMass != model.ballMass &&
	    !DictSetValue (dict.borrow (), "ball_mass", PyFloat_FromDouble (config.ballMass)))
		return nullptr;

	if (config.ballMaxSpeed != model.ballMaxSpeed &&
	    !DictSetValue (dict.borrow (), "ball_max_speed", PyFloat_FromDouble (config.ballMaxSpeed)))
		return nullptr;

	if (config.ballDrag != model.ballDrag &&
	    !DictSetValue (dict.borrow (), "ball_drag", PyFloat_FromDouble (config.ballDrag)))
		return nullptr;

	if (config.ballWorldFriction != model.ballWorldFriction &&
	    !DictSetValue (dict.borrow (), "ball_world_friction", PyFloat_FromDouble (config.ballWorldFriction)))
		return nullptr;

	if (config.ballWorldRestitution != model.ballWorldRestitution &&
	    !DictSetValue (dict.borrow (), "ball_world_restitution", PyFloat_FromDouble (config.ballWorldRestitution)))
		return nullptr;

	if (config.jumpAccel != model.jumpAccel &&
	    !DictSetValue (dict.borrow (), "jump_accel", PyFloat_FromDouble (config.jumpAccel)))
		return nullptr;

	if (config.jumpImmediateForce != model.jumpImmediateForce &&
	    !DictSetValue (dict.borrow (), "jump_immediate_force", PyFloat_FromDouble (config.jumpImmediateForce)))
		return nullptr;

	if (config.boostAccel != model.boostAccel &&
	    !DictSetValue (dict.borrow (), "boost_accel", PyFloat_FromDouble (config.boostAccel)))
		return nullptr;

	if (config.boostUsedPerSecond != model.boostUsedPerSecond &&
	    !DictSetValue (dict.borrow (), "boost_used_per_second", PyFloat_FromDouble (config.boostUsedPerSecond)))
		return nullptr;

	if (config.respawnDelay != model.respawnDelay &&
	    !DictSetValue (dict.borrow (), "respawn_delay", PyFloat_FromDouble (config.respawnDelay)))
		return nullptr;

	if (config.bumpCooldownTime != model.bumpCooldownTime &&
	    !DictSetValue (dict.borrow (), "bump_cooldown_time", PyFloat_FromDouble (config.bumpCooldownTime)))
		return nullptr;

	if (config.boostPadCooldown_Big != model.boostPadCooldown_Big &&
	    !DictSetValue (dict.borrow (), "boost_pad_cooldown_big", PyFloat_FromDouble (config.boostPadCooldown_Big)))
		return nullptr;

	if (config.boostPadCooldown_Small != model.boostPadCooldown_Small &&
	    !DictSetValue (dict.borrow (), "boost_pad_cooldown_small", PyFloat_FromDouble (config.boostPadCooldown_Small)))
		return nullptr;

	if (config.carSpawnBoostAmount != model.carSpawnBoostAmount &&
	    !DictSetValue (dict.borrow (), "car_spawn_boost_amount", PyFloat_FromDouble (config.carSpawnBoostAmount)))
		return nullptr;

	if (config.ballHitExtraForceScale != model.ballHitExtraForceScale &&
	    !DictSetValue (
	        dict.borrow (), "ball_hit_extra_force_scale", PyFloat_FromDouble (config.ballHitExtraForceScale)))
		return nullptr;

	if (config.bumpForceScale != model.bumpForceScale &&
	    !DictSetValue (dict.borrow (), "bump_force_scale", PyFloat_FromDouble (config.bumpForceScale)))
		return nullptr;

	if (config.ballRadius != model.ballRadius &&
	    !DictSetValue (dict.borrow (), "ball_radius", PyFloat_FromDouble (config.ballRadius)))
		return nullptr;

	if (config.unlimitedFlips != model.unlimitedFlips &&
	    !DictSetValue (dict.borrow (), "unlimited_flips", PyBool_FromLong (config.unlimitedFlips)))
		return nullptr;

	if (config.unlimitedDoubleJumps != model.unlimitedDoubleJumps &&
	    !DictSetValue (dict.borrow (), "unlimited_double_jumps", PyBool_FromLong (config.unlimitedDoubleJumps)))
		return nullptr;

	if (config.demoMode != model.demoMode &&
	    !DictSetValue (dict.borrow (), "demo_mode", PyLong_FromLong (static_cast<long> (config.demoMode))))
		return nullptr;

	if (config.enableTeamDemos != model.enableTeamDemos &&
	    !DictSetValue (dict.borrow (), "enable_team_demos", PyBool_FromLong (config.enableTeamDemos)))
		return nullptr;

	if (config.enableCarCarCollision != model.enableCarCarCollision &&
	    !DictSetValue (dict.borrow (), "enable_car_car_collision", PyBool_FromLong (config.enableCarCarCollision)))
		return nullptr;

	if (config.enableCarBallCollision != model.enableCarBallCollision &&
	    !DictSetValue (dict.borrow (), "enable_car_ball_collision", PyBool_FromLong (config.enableCarBallCollision)))
		return nullptr;

	if (config.goalBaseThresholdY != model.goalBaseThresholdY &&
	    !DictSetValue (dict.borrow (), "goal_base_threshold_y", PyFloat_FromDouble (config.goalBaseThresholdY)))
		return nullptr;

	return dict.gift ();
}

PyObject *MutatorConfig::Unpickle (MutatorConfig *self_, PyObject *dict_) noexcept
{
	if (!PyDict_Check (dict_))
	{
		PyErr_SetString (PyExc_ValueError, "Pickled object is not a dict");
		return nullptr;
	}

	auto const args = PyObjectRef::steal (PyTuple_New (0));
	if (!args)
		return nullptr;

	if (Init (self_, args.borrow (), dict_) != 0)
		return nullptr;

	Py_RETURN_NONE;
}

PyObject *MutatorConfig::Copy (MutatorConfig *self_) noexcept
{
	auto config = PyRef<MutatorConfig>::stealObject (New (Type, nullptr, nullptr));
	if (!config)
		return nullptr;

	PyRef<Vec>::assign (config->gravity, reinterpret_cast<PyObject *> (self_->gravity));

	config->config = ToMutatorConfig (self_);

	return config.giftObject ();
}

PyObject *MutatorConfig::DeepCopy (MutatorConfig *self_, PyObject *memo_) noexcept
{
	auto config = PyRef<MutatorConfig>::stealObject (New (Type, nullptr, nullptr));
	if (!config)
		return nullptr;

	PyRef<Vec>::assign (config->gravity, PyDeepCopy (self_->gravity, memo_));
	if (!config->gravity)
		return nullptr;

	config->config = ToMutatorConfig (self_);

	return config.giftObject ();
}

PyObject *MutatorConfig::Getgravity (MutatorConfig *self_, void *) noexcept
{
	return PyRef<Vec>::incRef (self_->gravity).giftObject ();
}

int MutatorConfig::Setgravity (MutatorConfig *self_, PyObject *value_, void *) noexcept
{
	if (!value_)
	{
		PyErr_SetString (PyExc_AttributeError, "can't delete 'gravity' attribute of 'RocketSim.MutatorConfig' objects");
		return -1;
	}

	if (!Py_IS_TYPE (value_, Vec::Type))
	{
		PyErr_SetString (PyExc_TypeError, "attribute value type must be RocketSim.Vec");
		return -1;
	}

	PyRef<Vec>::assign (self_->gravity, value_);

	return 0;
}
}
