<template>
	<view class="container">

		<view class="box_title">
			<text>用户注册</text>
		</view>
		<view class="goReg">
			<navigator url="../login/login"><text>已有账号?去登录</text></navigator>
		</view>
		<view class="box_form">
			<u-form :model="registerForm" ref="registerForm">
				<u-form-item label="用户账号" label-position="top" prop="userID">
					<u-input v-model="registerForm.userID" placeholder="请输入用户账号" />
				</u-form-item>
				<u-form-item label="用户密码" label-position="top" prop="passWord">
					<u-input v-model="registerForm.passWord" placeholder="请输入用户密码" type="password" />
				</u-form-item>
				<u-form-item label="确认密码" label-position="top" prop="repassWord">
					<u-input v-model="registerForm.repassWord" placeholder="请输入用户密码" type="password" />
				</u-form-item>
				<u-form-item label="手机号" label-position="top" prop="phone">
					<u-input v-model="registerForm.phone" placeholder="请输入用户手机号码" />
				</u-form-item>
				<u-form-item label="用户昵称" label-position="top" prop="nickName">
					<u-input v-model="registerForm.nickName" placeholder="请输入用户昵称" />
				</u-form-item>
				<u-form-item label="用户姓名" label-position="top" prop="userName">
					<u-input v-model="registerForm.userName" placeholder="请输入用户姓名" />
				</u-form-item>
				<u-form-item label="用户邮箱" label-position="top" prop="email">
					<u-input v-model="registerForm.email" placeholder="请输入用户邮箱" />
				</u-form-item>

			</u-form>

		</view>
		<!-- 		<view class="faceUpload">
			<u-form-item label="人脸信息上传" label-position="top" prop="faceInfo">
				
				<u-upload :file-list="fileList" ></u-upload>
			</u-form-item>
			
		</view> -->
		<view class="xieyi">

			<u-checkbox :label-disabled="true" v-model="xieyi.checked" :name="xieyi.name" :disabled="false">

				<text>我已阅读<text style="color: #007AFF;s" @click="OnXieyi">《用户协议》</text></text>
			</u-checkbox>
		</view>

		<view class="sub_reg">
			<u-button type="primary" @click="Onsub_reg">注册</u-button>
		</view>


	</view>
</template>

<script>
	import {
		register
	} from "../../common/api.js";
	import {
		MD5
	} from "../../js/MD5.js";

	export default {
		data() {

			//一次密码检验合法性
			const pwdCheck = async (rule, value, callback) => {
				let reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,16}$/
				if (value.length < 6) {
					this.changeFlag = 2;
					return callback(new Error('密码不能少于6位！'));
				} else if (value.length > 16) {
					this.changeFlag = 2;
					return callback(new Error('密码最长不能超过16位！'));
				} else if (!reg.test(value)) {
					this.changeFlag = 2;
					return callback(new Error('6-16位字符，同时包括数字和大小写字母三种组合'));
				} else {
					this.changeFlag = 1;
					callback()
				}
			};

			//二次密码检验正确性
			const pwdAgainCheck = async (rule, value, callback) => {
				if (value.length < 1) {
					this.changeAgainFlag = 2;
					return callback(new Error('密码不能为空！'));
				} else if (this.registerForm.passWord !== this.registerForm.repassWord) {
					this.changeAgainFlag = 2;
					return callback(new Error('密码不一致！'));
				} else {
					this.changeAgainFlag = 1;
					callback()
				}
			};

			//电话检验
			const phoneCheck = async (rule, value, callback) => {
				let telText = /^1\d{10}$/
				if (!telText.test(value)) {
					return callback(new Error('请正确输入手机号码'));
				} else {
					callback()
				}
			};

			return {
				fileList: [],
				registerForm: {
					userID: '',
					phone: '',
					passWord: '',
					repassWord: '',
					nickName: '',
					userName: '',
					email: '',
					// faceInfo:{}
				},
				rules: {
					phone: [{
						required: true,
						message: '请输入用户手机号码',
						// 可以单个或者同时写两个触发验证方式 
						trigger: ['change', 'blur'],
					}],

					passWord: [{
						required: true,
						// message: '请输入用户密码', 
						// 可以单个或者同时写两个触发验证方式 
						validator: pwdCheck,
						trigger: ['change', 'blur'],
					}],

					repassWord: [{
						required: true,
						// message: '用户密码必须输入',
						validator: pwdAgainCheck,
						trigger: 'blur'
					}],

					phone: [{
						required: true,
						// message: '用户手机号必须输入',
						validator: phoneCheck,
						trigger: 'blur'
					}],
				},
				xieyi: {
					checked: false,
					name: 'xieyi',
				}
			}
		},
		onReady() {
			this.$refs.registerForm.setRules(this.rules);
		},
		methods: {
			OnXieyi() {
				console.log('点击了用户协议')
			},
			Onsub_reg(e) {
				console.log('用户点击了注册')

				this.$refs.registerForm.validate(valid => {
					if (valid) {
						console.log('验证通过');
						console.log(this.registerForm);
						if (!this.xieyi.checked) {
							uni.showToast({
								title: '请勾选用户协议',
								icon: 'error'
							})
						} else {
							this.registerForm.MD5passWord = MD5(this.registerForm.passWord);
							this.registerForm.passWord = '';
							this.registerForm.repassWord = '';
							register(this.registerForm).then(res => {
								if (res.code == 0) {

									uni.showToast({
										title: res.msg
									});
									uni.navigateTo({
										url: '../login/login'
									});

									console.log('zhixingwanbi');
								}
							})
						}
					} else {
						console.log('验证失败');
					}
				});

			}
		}
	}
</script>

<style scoped lang="scss">
	.container {
		padding: 40rpx;

		.box_title {

			text {
				font-size: 22px;
				font-weight: 700;
			}
		}

		.box_form {
			// margin-top: 20rpx;

			.box_input {
				margin-bottom: 45rpx;

				.input_val {
					margin-top: 10rpx;
					border-bottom: .5px solid #eee;
					padding: 20rpx 0rpx;

					.pal {
						font-size: 15px;
						color: #aaaaaa;
					}
				}
			}

		}

		.xieyi {
			margin-top: 45rpx;
		}

		.sub_reg {
			margin-top: 45rpx;
		}

		.goReg {
			margin-top: 10rpx;
			color: #2979ff;
			font-size: 14px;
		}
	}
</style>
